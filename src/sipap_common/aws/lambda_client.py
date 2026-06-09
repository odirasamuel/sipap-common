"""AWS Lambda client wrapper for SIPAP.

Provides typed interface for Lambda function invocation with proper error handling.
"""

import json
from typing import Any, cast

from botocore.exceptions import BotoCoreError, ClientError

from sipap_common.aws.session import create_session
from sipap_common.exceptions import AWSServiceError


class LambdaClient:
    """Typed wrapper for AWS Lambda operations."""

    def __init__(
        self,
        region: str | None = None,
        lambda_client: Any | None = None,
    ) -> None:
        """Initialize Lambda client.

        Args:
            region: AWS region (defaults to 'us-east-1')
            lambda_client: Optional boto3 Lambda client for testing

        Raises:
            AWSServiceError: If client initialization fails
        """
        self.region = region or "us-east-1"

        if lambda_client is not None:
            self.lambda_client = lambda_client
        else:
            try:
                session = create_session(region=self.region)
                self.lambda_client = session.client("lambda")
            except Exception as e:
                raise AWSServiceError(f"Failed to initialize Lambda client: {e}")

    def invoke_function(
        self,
        function_name: str,
        payload: dict[str, Any],
        invocation_type: str = "RequestResponse",
        qualifier: str | None = None,
    ) -> dict[str, Any]:
        """Invoke a Lambda function.

        Args:
            function_name: Name or ARN of Lambda function
            payload: Dictionary to send as JSON payload
            invocation_type: 'RequestResponse' (sync), 'Event' (async), or
                'DryRun' (validation)
            qualifier: Version or alias to invoke (optional)

        Returns:
            Lambda invocation response with StatusCode, Payload, etc.

        Raises:
            AWSServiceError: If invocation fails

        Examples:
            >>> client = LambdaClient(region='us-east-1')
            >>> response = client.invoke_function(
            ...     'sports-data-mcp',
            ...     {'operation': 'get_matches', 'sport': 'soccer'}
            ... )
            >>> response['StatusCode']
            200
        """
        try:
            invoke_args: dict[str, Any] = {
                "FunctionName": function_name,
                "InvocationType": invocation_type,
                "Payload": json.dumps(payload),
            }

            if qualifier is not None:
                invoke_args["Qualifier"] = qualifier

            response = self.lambda_client.invoke(**invoke_args)
            return cast(dict[str, Any], response)

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(
                f"Failed to invoke Lambda function {function_name}: {e}"
            ) from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error invoking Lambda function {function_name}: {e}"
            ) from e
