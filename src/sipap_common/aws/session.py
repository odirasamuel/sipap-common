"""AWS session management for SIPAP.

Provides functions for creating boto3 sessions and AWS service clients
with proper credential and region management.
"""

from typing import Any

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from sipap_common.exceptions import AWSServiceError


def create_session(
    region: str | None = None,
    aws_access_key_id: str | None = None,
    aws_secret_access_key: str | None = None,
    aws_session_token: str | None = None,
) -> boto3.Session:
    """Create a boto3 session with optional credentials.

    Args:
        region: AWS region (e.g., 'us-east-1'). If None, uses AWS_DEFAULT_REGION
                environment variable or boto3 default.
        aws_access_key_id: AWS access key ID. If None, uses default credential chain.
        aws_secret_access_key: AWS secret access key. If None, uses default
                                credential chain.
        aws_session_token: AWS session token for temporary credentials.
                           If None, uses default credential chain.

    Returns:
        Configured boto3.Session instance

    Raises:
        AWSServiceError: If session creation fails

    Examples:
        >>> # Create session with default credentials
        >>> session = create_session(region='us-east-1')

        >>> # Create session with explicit credentials
        >>> session = create_session(
        ...     region='us-west-2',
        ...     aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
        ...     aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
        ... )
    """
    try:
        session = boto3.Session(
            region_name=region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
        )
        return session
    except Exception as e:
        raise AWSServiceError(f"Failed to create AWS session: {e}")


def get_aws_client(
    service_name: str,
    region: str | None = None,
    session: boto3.Session | None = None,
    aws_access_key_id: str | None = None,
    aws_secret_access_key: str | None = None,
    aws_session_token: str | None = None,
    **kwargs: Any,
) -> Any:
    """Get an AWS service client with proper configuration.

    Args:
        service_name: AWS service name (e.g., 's3', 'lambda', 'sqs')
        region: AWS region. If None, uses session's region or default.
        session: Existing boto3.Session to use. If None, creates new session.
        aws_access_key_id: AWS access key ID. Only used if session is None.
        aws_secret_access_key: AWS secret access key. Only used if session is None.
        aws_session_token: AWS session token. Only used if session is None.
        **kwargs: Additional arguments passed to session.client()

    Returns:
        Boto3 service client

    Raises:
        AWSServiceError: If client creation fails

    Examples:
        >>> # Get S3 client with default credentials
        >>> s3 = get_aws_client('s3', region='us-east-1')

        >>> # Get Lambda client from existing session
        >>> session = create_session(region='us-west-2')
        >>> lambda_client = get_aws_client('lambda', session=session)

        >>> # Get SQS client with explicit credentials
        >>> sqs = get_aws_client(
        ...     'sqs',
        ...     region='eu-west-1',
        ...     aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
        ...     aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
        ... )
    """
    try:
        # Use provided session or create new one
        if session is None:
            session = create_session(
                region=region,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token,
            )

        # Create client from session
        client = session.client(service_name, region_name=region, **kwargs)
        return client

    except (BotoCoreError, ClientError) as e:
        raise AWSServiceError(
            f"Failed to create AWS client for {service_name}: {e}"
        )
    except Exception as e:
        raise AWSServiceError(
            f"Unexpected error creating AWS client for {service_name}: {e}"
        )
