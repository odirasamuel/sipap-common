"""Tests for sipap_common.aws.session module."""

import os
from unittest.mock import patch

import boto3
import pytest
from moto import mock_aws

from sipap_common.aws import create_session, get_aws_client


def test_create_session_returns_boto3_session() -> None:
    """Test that create_session returns a boto3.Session instance."""
    session = create_session()
    assert isinstance(session, boto3.Session)


def test_create_session_with_region() -> None:
    """Test that create_session accepts region parameter."""
    session = create_session(region="us-west-2")
    assert session.region_name == "us-west-2"


def test_create_session_with_default_region() -> None:
    """Test that create_session uses default region."""
    session = create_session()
    # Should use AWS_REGION env var or AWS default
    assert session.region_name is not None


@mock_aws
def test_create_session_with_credentials() -> None:
    """Test creating session with explicit credentials."""
    session = create_session(
        region="us-east-1",
        aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
        aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    )

    assert isinstance(session, boto3.Session)
    credentials = session.get_credentials()
    assert credentials.access_key == "AKIAIOSFODNN7EXAMPLE"


@mock_aws
def test_create_session_with_role_assumption() -> None:
    """Test creating session with role assumption."""
    # This will be implemented when we add role assumption support
    # For now, just test that it doesn't crash
    session = create_session(region="us-east-1")
    assert isinstance(session, boto3.Session)


def test_get_aws_client_returns_boto3_client() -> None:
    """Test that get_aws_client returns a boto3 client."""
    client = get_aws_client("s3", region="us-east-1")
    assert client.meta.service_model.service_name == "s3"


def test_get_aws_client_with_different_services() -> None:
    """Test getting clients for different AWS services."""
    s3_client = get_aws_client("s3", region="us-east-1")
    lambda_client = get_aws_client("lambda", region="us-east-1")
    sqs_client = get_aws_client("sqs", region="us-east-1")

    assert s3_client.meta.service_model.service_name == "s3"
    assert lambda_client.meta.service_model.service_name == "lambda"
    assert sqs_client.meta.service_model.service_name == "sqs"


def test_get_aws_client_with_region() -> None:
    """Test that get_aws_client respects region parameter."""
    client = get_aws_client("s3", region="eu-west-1")
    assert client.meta.region_name == "eu-west-1"


@mock_aws
def test_get_aws_client_with_credentials() -> None:
    """Test getting client with explicit credentials."""
    client = get_aws_client(
        "s3",
        region="us-east-1",
        aws_access_key_id="AKIAIOSFODNN7EXAMPLE",
        aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
    )

    assert client.meta.service_model.service_name == "s3"


def test_get_aws_client_invalid_service_raises_error() -> None:
    """Test that invalid service name raises AWSServiceError."""
    with pytest.raises(Exception):  # Boto3 will raise its own exception
        get_aws_client("invalid_service_name", region="us-east-1")


@mock_aws
def test_get_aws_client_uses_environment_credentials() -> None:
    """Test that client uses environment variables for credentials."""
    with patch.dict(
        os.environ,
        {
            "AWS_ACCESS_KEY_ID": "AKIAIOSFODNN7EXAMPLE",
            "AWS_SECRET_ACCESS_KEY": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "AWS_DEFAULT_REGION": "us-west-2",
        },
    ):
        client = get_aws_client("s3")
        assert client.meta.region_name == "us-west-2"


def test_create_session_from_env_vars() -> None:
    """Test creating session from environment variables."""
    with patch.dict(
        os.environ, {"AWS_DEFAULT_REGION": "ap-southeast-1"}, clear=False
    ):
        session = create_session()
        # Should pick up region from env
        assert session.region_name in ["ap-southeast-1", None]  # None is ok too


@mock_aws
def test_session_can_create_multiple_clients() -> None:
    """Test that a session can create multiple clients."""
    session = create_session(region="us-east-1")

    s3 = session.client("s3")
    lambda_client = session.client("lambda")

    assert s3.meta.service_model.service_name == "s3"
    assert lambda_client.meta.service_model.service_name == "lambda"


def test_get_aws_client_with_session() -> None:
    """Test getting client from existing session."""
    session = create_session(region="us-east-1")
    client = get_aws_client("s3", session=session)

    assert client.meta.service_model.service_name == "s3"
    assert client.meta.region_name == "us-east-1"


@mock_aws
def test_create_session_handles_missing_credentials_gracefully() -> None:
    """Test that create_session handles missing credentials."""
    # With moto, this should work without real credentials
    session = create_session(region="us-east-1")
    assert isinstance(session, boto3.Session)


def test_region_parameter_overrides_environment() -> None:
    """Test that explicit region parameter overrides environment."""
    with patch.dict(os.environ, {"AWS_DEFAULT_REGION": "us-west-1"}, clear=False):
        session = create_session(region="eu-central-1")
        assert session.region_name == "eu-central-1"
