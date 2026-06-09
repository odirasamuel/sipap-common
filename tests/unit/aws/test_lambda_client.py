"""Tests for sipap_common.aws.lambda_client module."""

import json
from unittest.mock import Mock

import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from sipap_common.aws.lambda_client import LambdaClient
from sipap_common.exceptions import AWSServiceError


@mock_aws
def test_lambda_client_initializes_with_defaults() -> None:
    """Test that LambdaClient initializes with default configuration."""
    client = LambdaClient()
    assert client.region == "us-east-1"
    assert client.lambda_client is not None


@mock_aws
def test_lambda_client_initializes_with_custom_region() -> None:
    """Test that LambdaClient respects region parameter."""
    client = LambdaClient(region="eu-west-1")
    assert client.region == "eu-west-1"


def test_lambda_client_accepts_mock_client() -> None:
    """Test that LambdaClient accepts injected client for testing."""
    mock_client = Mock()
    client = LambdaClient(lambda_client=mock_client)
    assert client.lambda_client == mock_client


@mock_aws
def test_invoke_function_success() -> None:
    """Test successful Lambda function invocation."""
    # Create mock IAM role and Lambda function
    import boto3

    # Create IAM role first
    iam_client = boto3.client("iam", region_name="us-east-1")
    iam_client.create_role(
        RoleName="test-role",
        AssumeRolePolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        })
    )

    lambda_client = boto3.client("lambda", region_name="us-east-1")
    lambda_client.create_function(
        FunctionName="test-function",
        Runtime="python3.12",
        Role="arn:aws:iam::123456789012:role/test-role",
        Handler="index.handler",
        Code={"ZipFile": b"fake code"},
    )

    client = LambdaClient(region="us-east-1")
    payload = {"test": "data"}

    response = client.invoke_function("test-function", payload)

    assert response is not None
    assert "StatusCode" in response


@mock_aws
def test_invoke_function_with_request_response() -> None:
    """Test Lambda invocation with RequestResponse type."""
    import boto3

    # Create IAM role first
    iam_client = boto3.client("iam", region_name="us-east-1")
    iam_client.create_role(
        RoleName="test-role",
        AssumeRolePolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        })
    )

    lambda_client = boto3.client("lambda", region_name="us-east-1")
    lambda_client.create_function(
        FunctionName="test-function",
        Runtime="python3.12",
        Role="arn:aws:iam::123456789012:role/test-role",
        Handler="index.handler",
        Code={"ZipFile": b"fake code"},
    )

    client = LambdaClient(region="us-east-1")
    payload = {"operation": "test"}

    response = client.invoke_function(
        function_name="test-function", payload=payload, invocation_type="RequestResponse"
    )

    assert response["StatusCode"] == 200


def test_invoke_function_handles_client_error() -> None:
    """Test that invoke_function wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.invoke.side_effect = ClientError(
        {"Error": {"Code": "ResourceNotFoundException", "Message": "Function not found"}},
        "Invoke",
    )

    client = LambdaClient(lambda_client=mock_client)

    with pytest.raises(AWSServiceError, match="Failed to invoke Lambda function"):
        client.invoke_function("non-existent-function", {})


@mock_aws
def test_invoke_function_async() -> None:
    """Test Lambda invocation with Event (async) type."""
    import boto3

    # Create IAM role first
    iam_client = boto3.client("iam", region_name="us-east-1")
    iam_client.create_role(
        RoleName="test-role",
        AssumeRolePolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        })
    )

    lambda_client = boto3.client("lambda", region_name="us-east-1")
    lambda_client.create_function(
        FunctionName="async-function",
        Runtime="python3.12",
        Role="arn:aws:iam::123456789012:role/test-role",
        Handler="index.handler",
        Code={"ZipFile": b"fake code"},
    )

    client = LambdaClient(region="us-east-1")
    payload = {"async": True}

    response = client.invoke_function(
        function_name="async-function", payload=payload, invocation_type="Event"
    )

    assert response["StatusCode"] == 202  # Accepted for async


@mock_aws
def test_invoke_function_with_qualifier() -> None:
    """Test Lambda invocation with version/alias qualifier."""
    import boto3

    # Create IAM role first
    iam_client = boto3.client("iam", region_name="us-east-1")
    iam_client.create_role(
        RoleName="test-role",
        AssumeRolePolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }]
        })
    )

    lambda_client = boto3.client("lambda", region_name="us-east-1")
    lambda_client.create_function(
        FunctionName="versioned-function",
        Runtime="python3.12",
        Role="arn:aws:iam::123456789012:role/test-role",
        Handler="index.handler",
        Code={"ZipFile": b"fake code"},
    )

    client = LambdaClient(region="us-east-1")

    response = client.invoke_function(
        function_name="versioned-function", payload={}, qualifier="v1"
    )

    assert response["StatusCode"] == 200


def test_invoke_function_serializes_payload() -> None:
    """Test that payload is properly JSON serialized."""
    mock_client = Mock()
    mock_client.invoke.return_value = {"StatusCode": 200}

    client = LambdaClient(lambda_client=mock_client)
    payload = {"key": "value", "number": 123}

    client.invoke_function("test-function", payload)

    mock_client.invoke.assert_called_once()
    call_args = mock_client.invoke.call_args
    assert call_args[1]["Payload"] == json.dumps(payload)
