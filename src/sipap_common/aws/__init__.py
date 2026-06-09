"""AWS utilities module for SIPAP.

Provides AWS session management and typed client wrappers for AWS services.
"""

from sipap_common.aws.eventbridge_client import EventBridgeClient
from sipap_common.aws.lambda_client import LambdaClient
from sipap_common.aws.s3_client import S3Client
from sipap_common.aws.session import create_session, get_aws_client
from sipap_common.aws.sqs_client import SQSClient

__all__ = [
    "create_session",
    "get_aws_client",
    "LambdaClient",
    "SQSClient",
    "EventBridgeClient",
    "S3Client",
]
