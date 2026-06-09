"""AWS EventBridge client wrapper for SIPAP.

Provides typed interface for EventBridge event publishing with proper error handling.
"""

import json
from typing import Any, cast

from botocore.exceptions import BotoCoreError, ClientError

from sipap_common.aws.session import create_session
from sipap_common.exceptions import AWSServiceError


class EventBridgeClient:
    """Typed wrapper for AWS EventBridge operations."""

    def __init__(
        self,
        event_bus_name: str,
        region: str | None = None,
        eventbridge_client: Any | None = None,
    ) -> None:
        """Initialize EventBridge client.

        Args:
            event_bus_name: Name of the EventBridge event bus
            region: AWS region (defaults to 'us-east-1')
            eventbridge_client: Optional boto3 EventBridge client for testing

        Raises:
            AWSServiceError: If client initialization fails
        """
        self.event_bus_name = event_bus_name
        self.region = region or "us-east-1"

        if eventbridge_client is not None:
            self.eventbridge_client = eventbridge_client
        else:
            try:
                session = create_session(region=self.region)
                self.eventbridge_client = session.client("events")
            except Exception as e:
                raise AWSServiceError(f"Failed to initialize EventBridge client: {e}")

    def put_event(
        self,
        source: str,
        detail_type: str,
        detail: dict[str, Any],
        resources: list[str] | None = None,
    ) -> dict[str, Any]:
        """Publish a single event to EventBridge.

        Args:
            source: Event source identifier (e.g., 'sipap.orchestrator')
            detail_type: Type of event (e.g., 'MatchProcessed')
            detail: Event detail data as dictionary
            resources: Optional list of resource ARNs related to event

        Returns:
            Response with FailedEntryCount and Entries

        Raises:
            AWSServiceError: If event publishing fails

        Examples:
            >>> client = EventBridgeClient(event_bus_name='sipap-events')
            >>> response = client.put_event(
            ...     source='sipap.orchestrator',
            ...     detail_type='PredictionGenerated',
            ...     detail={'match_id': '12345', 'confidence': 0.85}
            ... )
            >>> response['FailedEntryCount']
            0
        """
        entry: dict[str, Any] = {
            "Source": source,
            "DetailType": detail_type,
            "Detail": json.dumps(detail),
            "EventBusName": self.event_bus_name,
        }

        if resources is not None:
            entry["Resources"] = resources

        try:
            response = self.eventbridge_client.put_events(Entries=[entry])
            return cast(dict[str, Any], response)

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to put event to EventBridge: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error putting event to EventBridge: {e}"
            ) from e

    def put_events(self, entries: list[dict[str, Any]]) -> dict[str, Any]:
        """Publish multiple events to EventBridge in a single call.

        Args:
            entries: List of event entry dictionaries with Source, DetailType,
                Detail, etc.

        Returns:
            Response with FailedEntryCount and Entries

        Raises:
            AWSServiceError: If event publishing fails

        Examples:
            >>> client = EventBridgeClient(event_bus_name='sipap-events')
            >>> events = [
            ...     {
            ...         'Source': 'sipap.orchestrator',
            ...         'DetailType': 'MatchProcessed',
            ...         'Detail': json.dumps({'match_id': '1'}),
            ...         'EventBusName': 'sipap-events'
            ...     },
            ...     {
            ...         'Source': 'sipap.predictor',
            ...         'DetailType': 'PredictionGenerated',
            ...         'Detail': json.dumps({'match_id': '1', 'prediction': 'home'}),
            ...         'EventBusName': 'sipap-events'
            ...     }
            ... ]
            >>> response = client.put_events(events)
            >>> response['FailedEntryCount']
            0
        """
        try:
            response = self.eventbridge_client.put_events(Entries=entries)
            return cast(dict[str, Any], response)

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to put events to EventBridge: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error putting events to EventBridge: {e}"
            ) from e
