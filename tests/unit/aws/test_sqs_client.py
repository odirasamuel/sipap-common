"""Tests for sipap_common.aws.sqs_client module."""

from unittest.mock import Mock

import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from sipap_common.aws.sqs_client import SQSClient
from sipap_common.exceptions import AWSServiceError


@mock_aws
def test_sqs_client_initializes_with_defaults() -> None:
    """Test that SQSClient initializes with default configuration."""
    client = SQSClient(queue_url="https://sqs.us-east-1.amazonaws.com/123/test-queue")
    assert client.queue_url == "https://sqs.us-east-1.amazonaws.com/123/test-queue"
    assert client.region == "us-east-1"
    assert client.sqs_client is not None


@mock_aws
def test_sqs_client_initializes_with_custom_region() -> None:
    """Test that SQSClient respects region parameter."""
    client = SQSClient(
        queue_url="https://sqs.eu-west-1.amazonaws.com/123/test-queue",
        region="eu-west-1",
    )
    assert client.region == "eu-west-1"


def test_sqs_client_accepts_mock_client() -> None:
    """Test that SQSClient accepts injected client for testing."""
    mock_client = Mock()
    client = SQSClient(
        queue_url="https://sqs.us-east-1.amazonaws.com/123/test",
        sqs_client=mock_client,
    )
    assert client.sqs_client == mock_client


@mock_aws
def test_send_message_success() -> None:
    """Test successful message sending to SQS."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="test-queue")["QueueUrl"]

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    message_body = {"test": "data", "count": 123}

    response = client.send_message(message_body)

    assert "MessageId" in response
    assert response["MessageId"] is not None


@mock_aws
def test_send_message_with_attributes() -> None:
    """Test sending message with custom attributes."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="test-queue")["QueueUrl"]

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    message_body = {"data": "value"}
    attributes = {"RequestId": {"StringValue": "req-123", "DataType": "String"}}

    response = client.send_message(message_body, message_attributes=attributes)

    assert "MessageId" in response


def test_send_message_handles_client_error() -> None:
    """Test that send_message wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.send_message.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}}, "SendMessage"
    )

    client = SQSClient(
        queue_url="https://sqs.us-east-1.amazonaws.com/123/test",
        sqs_client=mock_client,
    )

    with pytest.raises(AWSServiceError, match="Failed to send message to SQS"):
        client.send_message({"test": "data"})


@mock_aws
def test_receive_messages_success() -> None:
    """Test successful message receiving from SQS."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="test-queue")["QueueUrl"]

    # Send a test message
    sqs_client.send_message(QueueUrl=queue_url, MessageBody='{"test": "data"}')

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    messages = client.receive_messages(max_messages=1, wait_time_seconds=0)

    assert len(messages) == 1
    assert "test" in messages[0]["Body"]


@mock_aws
def test_receive_messages_empty_queue() -> None:
    """Test receiving from empty queue returns empty list."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="empty-queue")["QueueUrl"]

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    messages = client.receive_messages(max_messages=1, wait_time_seconds=0)

    assert messages == []


@mock_aws
def test_receive_messages_with_wait_time() -> None:
    """Test long polling with wait_time_seconds."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="test-queue")["QueueUrl"]

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    # Should not hang in tests (moto handles this)
    messages = client.receive_messages(max_messages=1, wait_time_seconds=5)

    assert isinstance(messages, list)


def test_receive_messages_handles_client_error() -> None:
    """Test that receive_messages wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.receive_message.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}},
        "ReceiveMessage",
    )

    client = SQSClient(
        queue_url="https://sqs.us-east-1.amazonaws.com/123/test",
        sqs_client=mock_client,
    )

    with pytest.raises(AWSServiceError, match="Failed to receive messages from SQS"):
        client.receive_messages()


@mock_aws
def test_delete_message_success() -> None:
    """Test successful message deletion from SQS."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="test-queue")["QueueUrl"]

    # Send and receive a message to get receipt handle
    sqs_client.send_message(QueueUrl=queue_url, MessageBody='{"test": "data"}')
    response = sqs_client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    receipt_handle = response["Messages"][0]["ReceiptHandle"]

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    # Should not raise
    client.delete_message(receipt_handle)


def test_delete_message_handles_client_error() -> None:
    """Test that delete_message wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.delete_message.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}},
        "DeleteMessage",
    )

    client = SQSClient(
        queue_url="https://sqs.us-east-1.amazonaws.com/123/test",
        sqs_client=mock_client,
    )

    with pytest.raises(AWSServiceError, match="Failed to delete message from SQS"):
        client.delete_message("receipt-handle-123")


@mock_aws
def test_receive_messages_max_count() -> None:
    """Test receiving multiple messages up to max_messages."""
    import boto3

    sqs_client = boto3.client("sqs", region_name="us-east-1")
    queue_url = sqs_client.create_queue(QueueName="test-queue")["QueueUrl"]

    # Send multiple messages
    for i in range(5):
        sqs_client.send_message(QueueUrl=queue_url, MessageBody=f'{{"msg": {i}}}')

    client = SQSClient(queue_url=queue_url, region="us-east-1")
    messages = client.receive_messages(max_messages=3, wait_time_seconds=0)

    # SQS may return up to max_messages (not guaranteed to return exactly max)
    assert len(messages) <= 3
    assert len(messages) > 0
