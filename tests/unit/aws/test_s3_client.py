"""Tests for sipap_common.aws.s3_client module."""

import json
from unittest.mock import Mock

import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from sipap_common.aws.s3_client import S3Client
from sipap_common.exceptions import AWSServiceError


@mock_aws
def test_s3_client_initializes_with_defaults() -> None:
    """Test that S3Client initializes with default configuration."""
    client = S3Client()
    assert client.region == "us-east-1"
    assert client.s3_client is not None


@mock_aws
def test_s3_client_initializes_with_custom_region() -> None:
    """Test that S3Client respects region parameter."""
    client = S3Client(region="eu-west-1")
    assert client.region == "eu-west-1"


def test_s3_client_accepts_mock_client() -> None:
    """Test that S3Client accepts injected client for testing."""
    mock_client = Mock()
    client = S3Client(s3_client=mock_client)
    assert client.s3_client == mock_client


@mock_aws
def test_put_object_success() -> None:
    """Test successful object upload to S3."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")

    client = S3Client(region="us-east-1")
    content = b"test data content"

    response = client.put_object(
        bucket="test-bucket", key="test-file.txt", body=content
    )

    assert "ETag" in response
    assert response["ETag"] is not None


@mock_aws
def test_put_object_with_metadata() -> None:
    """Test uploading object with custom metadata."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")

    client = S3Client(region="us-east-1")
    content = b"test data"
    metadata = {"request-id": "req-123", "sport": "soccer"}

    response = client.put_object(
        bucket="test-bucket", key="data.json", body=content, metadata=metadata
    )

    assert "ETag" in response


@mock_aws
def test_put_object_with_content_type() -> None:
    """Test uploading object with specified content type."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")

    client = S3Client(region="us-east-1")
    content = json.dumps({"test": "data"}).encode("utf-8")

    response = client.put_object(
        bucket="test-bucket",
        key="data.json",
        body=content,
        content_type="application/json",
    )

    assert "ETag" in response


def test_put_object_handles_client_error() -> None:
    """Test that put_object wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.put_object.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}}, "PutObject"
    )

    client = S3Client(s3_client=mock_client)

    with pytest.raises(AWSServiceError, match="Failed to put object to S3"):
        client.put_object(bucket="test-bucket", key="test.txt", body=b"data")


@mock_aws
def test_get_object_success() -> None:
    """Test successful object retrieval from S3."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")
    s3_client.put_object(Bucket="test-bucket", Key="test-file.txt", Body=b"test data")

    client = S3Client(region="us-east-1")
    content = client.get_object(bucket="test-bucket", key="test-file.txt")

    assert content == b"test data"


@mock_aws
def test_get_object_not_found() -> None:
    """Test get_object raises error for non-existent object."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")

    client = S3Client(region="us-east-1")

    with pytest.raises(AWSServiceError, match="Failed to get object from S3"):
        client.get_object(bucket="test-bucket", key="non-existent.txt")


def test_get_object_handles_client_error() -> None:
    """Test that get_object wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.get_object.side_effect = ClientError(
        {"Error": {"Code": "NoSuchKey", "Message": "Key not found"}}, "GetObject"
    )

    client = S3Client(s3_client=mock_client)

    with pytest.raises(AWSServiceError, match="Failed to get object from S3"):
        client.get_object(bucket="test-bucket", key="missing.txt")


@mock_aws
def test_delete_object_success() -> None:
    """Test successful object deletion from S3."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")
    s3_client.put_object(Bucket="test-bucket", Key="test-file.txt", Body=b"test data")

    client = S3Client(region="us-east-1")
    # Should not raise
    client.delete_object(bucket="test-bucket", key="test-file.txt")

    # Verify object is deleted
    with pytest.raises(ClientError):
        s3_client.get_object(Bucket="test-bucket", Key="test-file.txt")


def test_delete_object_handles_client_error() -> None:
    """Test that delete_object wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.delete_object.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}},
        "DeleteObject",
    )

    client = S3Client(s3_client=mock_client)

    with pytest.raises(AWSServiceError, match="Failed to delete object from S3"):
        client.delete_object(bucket="test-bucket", key="test.txt")


@mock_aws
def test_list_objects_success() -> None:
    """Test successful object listing from S3."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")
    s3_client.put_object(Bucket="test-bucket", Key="file1.txt", Body=b"data1")
    s3_client.put_object(Bucket="test-bucket", Key="file2.txt", Body=b"data2")

    client = S3Client(region="us-east-1")
    objects = client.list_objects(bucket="test-bucket")

    assert len(objects) == 2
    keys = [obj["Key"] for obj in objects]
    assert "file1.txt" in keys
    assert "file2.txt" in keys


@mock_aws
def test_list_objects_with_prefix() -> None:
    """Test object listing with prefix filter."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="test-bucket")
    s3_client.put_object(Bucket="test-bucket", Key="data/file1.json", Body=b"data1")
    s3_client.put_object(Bucket="test-bucket", Key="data/file2.json", Body=b"data2")
    s3_client.put_object(Bucket="test-bucket", Key="logs/file3.txt", Body=b"data3")

    client = S3Client(region="us-east-1")
    objects = client.list_objects(bucket="test-bucket", prefix="data/")

    assert len(objects) == 2
    assert all(obj["Key"].startswith("data/") for obj in objects)


@mock_aws
def test_list_objects_empty_bucket() -> None:
    """Test listing empty bucket returns empty list."""
    import boto3

    s3_client = boto3.client("s3", region_name="us-east-1")
    s3_client.create_bucket(Bucket="empty-bucket")

    client = S3Client(region="us-east-1")
    objects = client.list_objects(bucket="empty-bucket")

    assert objects == []


def test_list_objects_handles_client_error() -> None:
    """Test that list_objects wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.list_objects_v2.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}},
        "ListObjectsV2",
    )

    client = S3Client(s3_client=mock_client)

    with pytest.raises(AWSServiceError, match="Failed to list objects from S3"):
        client.list_objects(bucket="test-bucket")
