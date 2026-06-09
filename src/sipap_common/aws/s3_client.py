"""AWS S3 client wrapper for SIPAP.

Provides typed interface for S3 object operations with proper error handling.
"""

from typing import Any, cast

from botocore.exceptions import BotoCoreError, ClientError

from sipap_common.aws.session import create_session
from sipap_common.exceptions import AWSServiceError


class S3Client:
    """Typed wrapper for AWS S3 operations."""

    def __init__(
        self,
        region: str | None = None,
        s3_client: Any | None = None,
    ) -> None:
        """Initialize S3 client.

        Args:
            region: AWS region (defaults to 'us-east-1')
            s3_client: Optional boto3 S3 client for testing

        Raises:
            AWSServiceError: If client initialization fails
        """
        self.region = region or "us-east-1"

        if s3_client is not None:
            self.s3_client = s3_client
        else:
            try:
                session = create_session(region=self.region)
                self.s3_client = session.client("s3")
            except Exception as e:
                raise AWSServiceError(f"Failed to initialize S3 client: {e}")

    def put_object(
        self,
        bucket: str,
        key: str,
        body: bytes,
        content_type: str | None = None,
        metadata: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Upload an object to S3.

        Args:
            bucket: S3 bucket name
            key: Object key (path in bucket)
            body: Object content as bytes
            content_type: MIME type (e.g., 'application/json')
            metadata: Custom metadata key-value pairs

        Returns:
            Response with ETag, VersionId, etc.

        Raises:
            AWSServiceError: If upload fails

        Examples:
            >>> client = S3Client(region='us-east-1')
            >>> import json
            >>> data = json.dumps({'match_id': '12345'}).encode('utf-8')
            >>> response = client.put_object(
            ...     bucket='sipap-data',
            ...     key='predictions/match-12345.json',
            ...     body=data,
            ...     content_type='application/json'
            ... )
            >>> response['ETag']
            '"abc123..."'
        """
        try:
            put_args: dict[str, Any] = {
                "Bucket": bucket,
                "Key": key,
                "Body": body,
            }

            if content_type is not None:
                put_args["ContentType"] = content_type

            if metadata is not None:
                put_args["Metadata"] = metadata

            response = self.s3_client.put_object(**put_args)
            return cast(dict[str, Any], response)

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to put object to S3: {e}") from e
        except Exception as e:
            raise AWSServiceError(f"Unexpected error putting object to S3: {e}") from e

    def get_object(self, bucket: str, key: str) -> bytes:
        """Download an object from S3.

        Args:
            bucket: S3 bucket name
            key: Object key (path in bucket)

        Returns:
            Object content as bytes

        Raises:
            AWSServiceError: If download fails or object not found

        Examples:
            >>> client = S3Client(region='us-east-1')
            >>> content = client.get_object(
            ...     bucket='sipap-data',
            ...     key='predictions/match-12345.json'
            ... )
            >>> import json
            >>> data = json.loads(content.decode('utf-8'))
        """
        try:
            response = self.s3_client.get_object(Bucket=bucket, Key=key)
            return cast(bytes, response["Body"].read())

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to get object from S3: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error getting object from S3: {e}"
            ) from e

    def delete_object(self, bucket: str, key: str) -> None:
        """Delete an object from S3.

        Args:
            bucket: S3 bucket name
            key: Object key (path in bucket)

        Raises:
            AWSServiceError: If deletion fails

        Examples:
            >>> client = S3Client(region='us-east-1')
            >>> client.delete_object(
            ...     bucket='sipap-data',
            ...     key='temp/old-prediction.json'
            ... )
        """
        try:
            self.s3_client.delete_object(Bucket=bucket, Key=key)

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to delete object from S3: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error deleting object from S3: {e}"
            ) from e

    def list_objects(
        self, bucket: str, prefix: str | None = None, max_keys: int = 1000
    ) -> list[dict[str, Any]]:
        """List objects in an S3 bucket.

        Args:
            bucket: S3 bucket name
            prefix: Optional prefix to filter objects
            max_keys: Maximum number of keys to return (default 1000)

        Returns:
            List of object dictionaries with Key, Size, LastModified, etc.

        Raises:
            AWSServiceError: If listing fails

        Examples:
            >>> client = S3Client(region='us-east-1')
            >>> objects = client.list_objects(
            ...     bucket='sipap-data',
            ...     prefix='predictions/soccer/'
            ... )
            >>> for obj in objects:
            ...     print(obj['Key'], obj['Size'])
        """
        try:
            list_args: dict[str, Any] = {
                "Bucket": bucket,
                "MaxKeys": max_keys,
            }

            if prefix is not None:
                list_args["Prefix"] = prefix

            response = self.s3_client.list_objects_v2(**list_args)
            return cast(list[dict[str, Any]], response.get("Contents", []))

        except (BotoCoreError, ClientError) as e:
            raise AWSServiceError(f"Failed to list objects from S3: {e}") from e
        except Exception as e:
            raise AWSServiceError(
                f"Unexpected error listing objects from S3: {e}"
            ) from e
