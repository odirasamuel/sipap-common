"""AWS SQS client wrapper for SIPAP.

Provides typed interface for SQS queue operations with proper error handling.
"""

import json
from typing import Any, cast

from botocore.exceptions import BotoCoreError, ClientError

from sipap_common.aws.session import create_session
from sipap_common.exceptions import AWSServiceError


class SQSClient:
    """Typed wrapper for AWS SQS operations."""

    def __init__(
        self,
        queue_url: str,
        region: str | None = None,
        sqs_client: Any | None = None,
    ) -> None:
        """Initialize SQS client.

        Args:
            queue_url: Full URL of the SQS queue
            region: AWS region (defaults to 'us-east-1')
            sqs_client: Optional boto3 SQS client for testing

        Raises:
            AWSServiceError: If client initialization fails
        """
        self.queue_url = queue_url
        self.region = region or "us-east-1"

        if sqs_client is not None:
            self.sqs_client = sqs_client
        else:
            try:
                session = create_session(region=self.region)
                self.sqs_client = session.client("sqs")
            except Exception as e:
                raise AWSServiceError(f"Failed to initialize SQS client: {e}")

    def send_message(
        self,
        message_body: dict[str, Any],
        message_attributes: dict[str, Any] | None = None,
        delay_seconds: int = 0,
    ) -> dict[str, Any]:
        """Send a message to the SQS queue.

        Args:
            message_body: Dictionary to send as JSON message body
            message_attributes: Optional message attributes
            delay_seconds: Delay before message becomes available (0-900)

        Returns:
            Response with MessageId and MD5OfMessageBody

        Raises:
            AWSServiceError: If sending fails

        Examples:
            >>> client = SQSClient(
            ...     queue_url='https://sqs.us-east-1.amazonaws.com/123/predictions'
            ... )
            >>> response = client.send_message({'match_id': '12345', 'sport': 'soccer'})
            >>> response['MessageId']
            'abc123...'
        """
        try:
            send_args: dict[str, Any] = {
                "QueueUrl": self.queue_url,
                "MessageBody": json.dumps(message_body),
                "DelaySeconds": delay_seconds,
            }

            if message_attributes is not None:
                send_args["MessageAttributes"] = message_attributes

            response = self.sqs_client.send_message(**send_args)
            return cast(dict[str, Any], response)

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to send message to SQS: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error sending message to SQS: {e}"
            ) from e

    def receive_messages(
        self,
        max_messages: int = 1,
        wait_time_seconds: int = 20,
        visibility_timeout: int | None = None,
    ) -> list[dict[str, Any]]:
        """Receive messages from the SQS queue.

        Args:
            max_messages: Maximum number of messages to receive (1-10)
            wait_time_seconds: Long polling wait time (0-20)
            visibility_timeout: Visibility timeout in seconds (optional)

        Returns:
            List of message dictionaries with Body, ReceiptHandle, etc.

        Raises:
            AWSServiceError: If receiving fails

        Examples:
            >>> client = SQSClient(queue_url='https://sqs.us-east-1.amazonaws.com/...')
            >>> messages = client.receive_messages(max_messages=5, wait_time_seconds=10)
            >>> for msg in messages:
            ...     body = json.loads(msg['Body'])
            ...     print(body['match_id'])
        """
        try:
            receive_args: dict[str, Any] = {
                "QueueUrl": self.queue_url,
                "MaxNumberOfMessages": max_messages,
                "WaitTimeSeconds": wait_time_seconds,
                "AttributeNames": ["All"],
                "MessageAttributeNames": ["All"],
            }

            if visibility_timeout is not None:
                receive_args["VisibilityTimeout"] = visibility_timeout

            response = self.sqs_client.receive_message(**receive_args)
            return cast(list[dict[str, Any]], response.get("Messages", []))

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to receive messages from SQS: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error receiving messages from SQS: {e}"
            ) from e

    def delete_message(self, receipt_handle: str) -> None:
        """Delete a message from the SQS queue.

        Args:
            receipt_handle: Receipt handle from received message

        Raises:
            AWSServiceError: If deletion fails

        Examples:
            >>> client = SQSClient(queue_url='https://sqs.us-east-1.amazonaws.com/...')
            >>> messages = client.receive_messages()
            >>> for msg in messages:
            ...     # Process message
            ...     client.delete_message(msg['ReceiptHandle'])
        """
        try:
            self.sqs_client.delete_message(
                QueueUrl=self.queue_url, ReceiptHandle=receipt_handle
            )

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to delete message from SQS: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error deleting message from SQS: {e}"
            ) from e
