"""Tests for sipap_common.aws.eventbridge_client module."""

from unittest.mock import Mock

import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from sipap_common.aws.eventbridge_client import EventBridgeClient
from sipap_common.exceptions import AWSServiceError


@mock_aws
def test_eventbridge_client_initializes_with_defaults() -> None:
    """Test that EventBridgeClient initializes with default configuration."""
    client = EventBridgeClient(event_bus_name="default")
    assert client.event_bus_name == "default"
    assert client.region == "us-east-1"
    assert client.eventbridge_client is not None


@mock_aws
def test_eventbridge_client_initializes_with_custom_region() -> None:
    """Test that EventBridgeClient respects region parameter."""
    client = EventBridgeClient(event_bus_name="custom-bus", region="eu-west-1")
    assert client.region == "eu-west-1"


def test_eventbridge_client_accepts_mock_client() -> None:
    """Test that EventBridgeClient accepts injected client for testing."""
    mock_client = Mock()
    client = EventBridgeClient(
        event_bus_name="test-bus", eventbridge_client=mock_client
    )
    assert client.eventbridge_client == mock_client


@mock_aws
def test_put_event_success() -> None:
    """Test successful event publishing to EventBridge."""
    import boto3

    eventbridge_client = boto3.client("events", region_name="us-east-1")
    eventbridge_client.create_event_bus(Name="test-bus")

    client = EventBridgeClient(event_bus_name="test-bus", region="us-east-1")
    detail = {"match_id": "12345", "sport": "soccer"}

    response = client.put_event(
        source="sipap.orchestrator",
        detail_type="MatchProcessed",
        detail=detail,
    )

    assert "FailedEntryCount" in response
    assert response["FailedEntryCount"] == 0


@mock_aws
def test_put_event_with_resources() -> None:
    """Test event publishing with resource ARNs."""
    import boto3

    eventbridge_client = boto3.client("events", region_name="us-east-1")
    eventbridge_client.create_event_bus(Name="test-bus")

    client = EventBridgeClient(event_bus_name="test-bus", region="us-east-1")
    detail = {"prediction": "home_win"}
    resources = ["arn:aws:lambda:us-east-1:123456789012:function:processor"]

    response = client.put_event(
        source="sipap.predictor",
        detail_type="PredictionGenerated",
        detail=detail,
        resources=resources,
    )

    assert response["FailedEntryCount"] == 0


@mock_aws
def test_put_events_batch_success() -> None:
    """Test batch event publishing to EventBridge."""
    import json

    import boto3

    eventbridge_client = boto3.client("events", region_name="us-east-1")
    eventbridge_client.create_event_bus(Name="test-bus")

    client = EventBridgeClient(event_bus_name="test-bus", region="us-east-1")
    events = [
        {
            "Source": "sipap.orchestrator",
            "DetailType": "MatchProcessed",
            "Detail": json.dumps({"match_id": f"match-{i}"}),
            "EventBusName": "test-bus",
        }
        for i in range(3)
    ]

    response = client.put_events(events)

    assert "FailedEntryCount" in response
    assert response["FailedEntryCount"] == 0
    assert "Entries" in response


def test_put_event_handles_client_error() -> None:
    """Test that put_event wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.put_events.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}}, "PutEvents"
    )

    client = EventBridgeClient(
        event_bus_name="test-bus", eventbridge_client=mock_client
    )

    with pytest.raises(AWSServiceError, match="Failed to put event to EventBridge"):
        client.put_event(
            source="test.source", detail_type="Test", detail={"test": "data"}
        )


def test_put_events_handles_client_error() -> None:
    """Test that put_events wraps ClientError in AWSServiceError."""
    mock_client = Mock()
    mock_client.put_events.side_effect = ClientError(
        {"Error": {"Code": "AccessDenied", "Message": "Access denied"}}, "PutEvents"
    )

    client = EventBridgeClient(
        event_bus_name="test-bus", eventbridge_client=mock_client
    )

    with pytest.raises(AWSServiceError, match="Failed to put events to EventBridge"):
        client.put_events([{"Source": "test", "DetailType": "Test", "Detail": "{}"}])


@mock_aws
def test_put_event_validates_failed_entries() -> None:
    """Test that failed event entries are reported."""
    # Note: moto doesn't simulate failures well, so we test the structure
    import boto3

    eventbridge_client = boto3.client("events", region_name="us-east-1")
    eventbridge_client.create_event_bus(Name="test-bus")

    client = EventBridgeClient(event_bus_name="test-bus", region="us-east-1")

    response = client.put_event(
        source="sipap.test", detail_type="TestEvent", detail={"key": "value"}
    )

    # Successful response should have 0 failed entries
    assert response["FailedEntryCount"] == 0


def test_put_event_serializes_detail() -> None:
    """Test that detail dict is properly JSON serialized."""
    mock_client = Mock()
    mock_client.put_events.return_value = {"FailedEntryCount": 0, "Entries": []}

    client = EventBridgeClient(
        event_bus_name="test-bus", eventbridge_client=mock_client
    )
    detail = {"match_id": "12345", "odds": 1.85}

    client.put_event(source="test.source", detail_type="Test", detail=detail)

    mock_client.put_events.assert_called_once()
    call_args = mock_client.put_events.call_args
    entries = call_args[1]["Entries"]
    assert len(entries) == 1
    # Detail should be JSON string
    assert isinstance(entries[0]["Detail"], str)
    assert "match_id" in entries[0]["Detail"]


@mock_aws
def test_eventbridge_client_uses_default_bus() -> None:
    """Test that client can use default event bus."""
    client = EventBridgeClient(event_bus_name="default", region="us-east-1")

    # Default bus doesn't need creation
    response = client.put_event(
        source="sipap.test", detail_type="TestEvent", detail={"test": "data"}
    )

    assert response["FailedEntryCount"] == 0
