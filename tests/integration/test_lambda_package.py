"""Integration tests for Lambda package build process.

Tests cover:
1. Package zip structure validation
2. Import verification from built package
3. Python version resolution (mocked endoflife.date API)
4. S3 upload simulation (mocked S3 with moto)
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import zipfile
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING
from unittest.mock import Mock, patch

import boto3
import pytest
from moto import mock_aws

if TYPE_CHECKING:
    from collections.abc import Generator

# Test fixtures
MOCK_PYTHON_VERSIONS_RESPONSE = {
    "result": {
        "releases": [
            {"name": "python3.14", "isEol": False, "version": "3.14"},
            {"name": "python3.13", "isEol": False, "version": "3.13"},
            {"name": "python3.12", "isEol": False, "version": "3.12"},
            {"name": "python3.11", "isEol": False, "version": "3.11"},
            {"name": "python3.10", "isEol": True, "version": "3.10"},
            {"name": "python3.9", "isEol": True, "version": "3.9"},
        ]
    }
}

EXPECTED_MATRIX_OUTPUT = {
    "include": [
        {"python": "3.14"},
        {"python": "3.13"},
        {"python": "3.12"},
    ]
}


@pytest.fixture
def repo_root() -> Path:
    """Get repository root directory."""
    # Navigate up from tests/integration to repo root
    return Path(__file__).parent.parent.parent


@pytest.fixture
def build_script(repo_root: Path) -> Path:
    """Get path to build script."""
    script_path = repo_root / "scripts" / "build-lambda-package.sh"
    assert script_path.exists(), f"Build script not found at {script_path}"
    return script_path


@pytest.fixture
def temp_build_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """Create temporary build directory."""
    build_dir = tmp_path / "build"
    build_dir.mkdir(exist_ok=True)
    yield build_dir


@pytest.fixture
def mock_s3() -> Generator[boto3.client, None, None]:
    """Create mocked S3 client."""
    with mock_aws():
        s3_client = boto3.client("s3", region_name="us-east-1")
        # Create test bucket
        s3_client.create_bucket(Bucket="sipap-lambda-packages-dev")
        yield s3_client


class TestBuildScript:
    """Test Lambda package build script."""

    def test_build_script_exists(self, build_script: Path) -> None:
        """Test that build script exists and is executable."""
        assert build_script.exists()
        assert os.access(build_script, os.X_OK), "Build script is not executable"

    def test_build_script_creates_layer_zip(
        self, build_script: Path, repo_root: Path, tmp_path: Path
    ) -> None:
        """Test that build script creates a valid layer.zip file."""
        # Change to repo root for build
        original_dir = os.getcwd()
        try:
            os.chdir(repo_root)

            # Run build script with Python version
            python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
            result = subprocess.run(
                [str(build_script), python_version],
                capture_output=True,
                text=True,
                check=False,
            )

            # Check that script succeeded
            assert (
                result.returncode == 0
            ), f"Build script failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

            # Check that zip file was created
            expected_zip = repo_root / f"sipap_common_layer_py{python_version}.zip"
            assert expected_zip.exists(), f"Layer zip not created at {expected_zip}"

            # Verify zip structure
            with zipfile.ZipFile(expected_zip, "r") as zf:
                namelist = zf.namelist()
                # Should have python/ directory with packages
                python_files = [n for n in namelist if n.startswith("python/")]
                assert len(python_files) > 0, "No files in python/ directory"

                # Should include sipap_common package
                sipap_common_files = [
                    n for n in namelist if "sipap_common" in n and n.endswith(".py")
                ]
                assert (
                    len(sipap_common_files) > 0
                ), "sipap_common package not found in layer"

            # Cleanup
            expected_zip.unlink()

        finally:
            os.chdir(original_dir)

    def test_package_imports_successfully(
        self, build_script: Path, repo_root: Path, tmp_path: Path
    ) -> None:
        """Test that packages can be imported from built layer."""
        # Build package
        original_dir = os.getcwd()
        try:
            os.chdir(repo_root)

            python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
            result = subprocess.run(
                [str(build_script), python_version],
                capture_output=True,
                text=True,
                check=False,
            )

            assert result.returncode == 0, "Build script failed"

            expected_zip = repo_root / f"sipap_common_layer_py{python_version}.zip"
            assert expected_zip.exists()

            # Extract to temp directory
            extract_dir = tmp_path / "layer"
            with zipfile.ZipFile(expected_zip, "r") as zf:
                zf.extractall(extract_dir)

            # Test import by adding to sys.path and importing
            sys.path.insert(0, str(extract_dir / "python"))
            try:
                # Import sipap_common package
                import sipap_common  # type: ignore[import-not-found]

                # Verify key functions exist
                assert hasattr(sipap_common, "get_logger")
                assert hasattr(sipap_common, "load_config")

            except ImportError as e:
                pytest.fail(f"Failed to import sipap_common from layer: {e}")
            finally:
                sys.path.pop(0)

            # Cleanup
            expected_zip.unlink()

        finally:
            os.chdir(original_dir)


class TestVersionResolution:
    """Test Python version resolution from endoflife.date API."""

    @patch("urllib.request.urlopen")
    def test_version_resolution_api_call(self, mock_urlopen: Mock) -> None:
        """Test that version resolution correctly parses endoflife.date API response."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.read.return_value = json.dumps(MOCK_PYTHON_VERSIONS_RESPONSE).encode()
        mock_response.__enter__ = Mock(return_value=mock_response)
        mock_response.__exit__ = Mock(return_value=False)
        mock_urlopen.return_value = mock_response

        # Simulate version resolution logic (same as in workflow)
        import urllib.request

        with urllib.request.urlopen("https://endoflife.date/api/v1/products/aws-lambda") as response:
            data = json.loads(response.read().decode())

        # Filter for Python runtimes that are not EOL
        python_releases = [
            r for r in data["result"]["releases"] if r["name"].startswith("python") and not r["isEol"]
        ]

        # Sort by version (descending) and take top 3
        python_releases_sorted = sorted(
            python_releases,
            key=lambda r: [int(x) for x in r["name"].replace("python", "").split(".")],
            reverse=True,
        )
        top_3 = python_releases_sorted[:3]

        # Create matrix format
        matrix = {
            "include": [
                {"python": release["name"].replace("python", "")} for release in top_3
            ]
        }

        # Verify result matches expected output
        assert matrix == EXPECTED_MATRIX_OUTPUT

    def test_matrix_format_validation(self) -> None:
        """Test that matrix output has correct format."""
        matrix = EXPECTED_MATRIX_OUTPUT

        # Should have 'include' key
        assert "include" in matrix

        # Should have 3 entries
        assert len(matrix["include"]) == 3

        # Each entry should have 'python' key
        for entry in matrix["include"]:
            assert "python" in entry
            # Python version should match format: X.Y
            python_version = entry["python"]
            assert python_version.count(".") == 1
            major, minor = python_version.split(".")
            assert major.isdigit()
            assert minor.isdigit()
            assert int(major) == 3  # Python 3.x


class TestS3Upload:
    """Test S3 upload functionality with mocked AWS."""

    def test_s3_upload_with_metadata(self, mock_s3: boto3.client) -> None:
        """Test uploading layer package to S3 with metadata."""
        # Create a test zip file
        test_zip_content = b"PK\x03\x04test zip content"
        package_name = "sipap_common"
        python_version = "3.12"
        git_sha = hashlib.sha256(b"test-commit").hexdigest()[:8]
        build_date = datetime.now(UTC).isoformat()

        # Upload to S3
        s3_key = f"{package_name}/python_{python_version}/layer.zip"
        mock_s3.put_object(
            Bucket="sipap-lambda-packages-dev",
            Key=s3_key,
            Body=test_zip_content,
            Metadata={
                "git-sha": git_sha,
                "python-version": python_version,
                "package-name": package_name,
                "build-date": build_date,
            },
        )

        # Verify object exists
        response = mock_s3.head_object(
            Bucket="sipap-lambda-packages-dev",
            Key=s3_key,
        )

        # Verify metadata
        assert response["Metadata"]["git-sha"] == git_sha
        assert response["Metadata"]["python-version"] == python_version
        assert response["Metadata"]["package-name"] == package_name
        assert "build-date" in response["Metadata"]

        # Verify content
        obj = mock_s3.get_object(
            Bucket="sipap-lambda-packages-dev",
            Key=s3_key,
        )
        assert obj["Body"].read() == test_zip_content

    def test_s3_key_structure(self, mock_s3: boto3.client) -> None:
        """Test that S3 keys follow expected structure: <package>/python_<version>/layer.zip."""
        test_packages = [
            ("sipap_common", "3.12"),
            ("sipap_common", "3.13"),
            ("sipap_serverlesshandler", "3.12"),
            ("data", "3.12"),
            ("intelligence", "3.12"),
        ]

        for package_name, python_version in test_packages:
            s3_key = f"{package_name}/python_{python_version}/layer.zip"

            # Upload test object
            mock_s3.put_object(
                Bucket="sipap-lambda-packages-dev",
                Key=s3_key,
                Body=b"test",
                Metadata={
                    "package-name": package_name,
                    "python-version": python_version,
                },
            )

            # Verify key structure
            parts = s3_key.split("/")
            assert len(parts) == 3
            assert parts[0] == package_name
            assert parts[1] == f"python_{python_version}"
            assert parts[2] == "layer.zip"

    def test_multiple_python_versions_coexist(self, mock_s3: boto3.client) -> None:
        """Test that multiple Python versions can coexist in S3."""
        package_name = "sipap_common"
        python_versions = ["3.12", "3.13", "3.14"]

        # Upload packages for each Python version
        for python_version in python_versions:
            s3_key = f"{package_name}/python_{python_version}/layer.zip"
            mock_s3.put_object(
                Bucket="sipap-lambda-packages-dev",
                Key=s3_key,
                Body=f"content-{python_version}".encode(),
                Metadata={"python-version": python_version},
            )

        # Verify all versions exist
        for python_version in python_versions:
            s3_key = f"{package_name}/python_{python_version}/layer.zip"
            response = mock_s3.head_object(
                Bucket="sipap-lambda-packages-dev",
                Key=s3_key,
            )
            assert response["Metadata"]["python-version"] == python_version


class TestPackageStructure:
    """Test Lambda package structure validation."""

    def test_layer_directory_structure(self, tmp_path: Path) -> None:
        """Test that layer follows AWS Lambda layer directory structure."""
        # Create test layer structure
        layer_dir = tmp_path / "layer"
        python_dir = layer_dir / "python"
        python_dir.mkdir(parents=True)

        # Add test package
        (python_dir / "sipap_common").mkdir()
        (python_dir / "sipap_common" / "__init__.py").write_text("# Test package")
        (python_dir / "sipap_common" / "logging.py").write_text("# Logging module")

        # Create zip
        zip_path = tmp_path / "layer.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, _dirs, files in os.walk(python_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(layer_dir)
                    zf.write(file_path, arcname)

        # Verify zip structure
        with zipfile.ZipFile(zip_path, "r") as zf:
            namelist = zf.namelist()

            # All files should be under python/
            assert all(n.startswith("python/") for n in namelist)

            # Should have sipap_common package
            assert "python/sipap_common/__init__.py" in namelist
            assert "python/sipap_common/logging.py" in namelist

    def test_no_pycache_in_package(self, tmp_path: Path) -> None:
        """Test that __pycache__ directories are excluded from package."""
        # Create test structure with __pycache__
        layer_dir = tmp_path / "layer"
        python_dir = layer_dir / "python"
        package_dir = python_dir / "sipap_common"
        pycache_dir = package_dir / "__pycache__"

        pycache_dir.mkdir(parents=True)
        (package_dir / "__init__.py").write_text("# Test")
        (pycache_dir / "__init__.cpython-312.pyc").write_bytes(b"test")

        # Simulate cleanup (as done in build script)
        import shutil

        for root, dirs, _files in os.walk(layer_dir):
            if "__pycache__" in dirs:
                shutil.rmtree(Path(root) / "__pycache__")

        # Create zip
        zip_path = tmp_path / "layer.zip"
        with zipfile.ZipFile(zip_path, "w") as zf:
            for root, _dirs, files in os.walk(python_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(layer_dir)
                    zf.write(file_path, arcname)

        # Verify no __pycache__ in zip
        with zipfile.ZipFile(zip_path, "r") as zf:
            namelist = zf.namelist()
            assert not any("__pycache__" in n for n in namelist)
            assert not any(n.endswith(".pyc") for n in namelist)
