"""AWS integration examples using sipap-common.

This example demonstrates AWS service integrations:
1. Session management
2. Lambda client
3. SQS client
4. EventBridge client
5. S3 client

Note: These examples use moto for mocking AWS services.
"""

import os
import json
from sipap_common.aws import (
    create_session,
    get_aws_client,
    LambdaClient,
    SQSClient,
    EventBridgeClient,
    S3Client
)
from sipap_common.logging import get_logger, set_log_context
from sipap_common.utils import current_timestamp, safe_json_dumps
from sipap_common.exceptions import AWSServiceError


def setup_logging():
    """Setup structured logging for AWS operations."""
    set_log_context(
        request_id="req-aws-example",
        component="aws-integration"
    )


def example_session_management():
    """Example: Create and manage AWS sessions."""
    print("\n=== AWS Session Management ===")

    logger = get_logger("aws.session")

    # Create session with default profile
    session = create_session(region="us-east-1")
    logger.info("Session created", region="us-east-1")
    print(f"Region: {session.region_name}")

    # Create session with specific profile
    # session = create_session(region="us-west-2", profile="production")

    # Get generic AWS client
    s3_client = get_aws_client("s3", session=session)
    logger.info("S3 client created")

    print("✅ Session management demonstrated")


def example_lambda_client():
    """Example: Use Lambda client for function operations."""
    print("\n=== Lambda Client ===")

    logger = get_logger("aws.lambda")

    # Note: In production, use actual AWS credentials
    print("Note: This shows the API pattern. Use moto for testing.")

    # Create Lambda client
    session = create_session(region="us-east-1")
    lambda_client = LambdaClient(session)

    # Example: Invoke Lambda function
    function_name = "sipap-match-processor"
    payload = {
        "match_id": "match-12345",
        "action": "process",
        "timestamp": current_timestamp()
    }

    logger.info("Would invoke Lambda function", function=function_name)
    print(f"Function: {function_name}")
    print(f"Payload: {safe_json_dumps(payload, pretty=True)}")

    # API pattern:
    # response = lambda_client.invoke_function(
    #     function_name=function_name,
    #     payload=payload,
    #     invocation_type="RequestResponse"
    # )
    # print(f"Response: {response}")

    print("✅ Lambda client API demonstrated")


def example_sqs_client():
    """Example: Use SQS client for message queue operations."""
    print("\n=== SQS Client ===")

    logger = get_logger("aws.sqs")

    # Create SQS client
    session = create_session(region="us-east-1")
    sqs_client = SQSClient(session)

    # Example: Send message to queue
    queue_url = "https://sqs.us-east-1.amazonaws.com/123456789012/sipap-predictions"
    message = {
        "match_id": "match-67890",
        "prediction": {
            "home_score": 2,
            "away_score": 1,
            "confidence": 0.75
        },
        "timestamp": current_timestamp()
    }

    logger.info("Would send SQS message", queue=queue_url)
    print(f"Queue: {queue_url}")
    print(f"Message: {safe_json_dumps(message, pretty=True)}")

    # API pattern:
    # message_id = sqs_client.send_message(
    #     queue_url=queue_url,
    #     message_body=message
    # )
    # print(f"Message ID: {message_id}")

    # Example: Receive and delete messages
    # messages = sqs_client.receive_messages(
    #     queue_url=queue_url,
    #     max_messages=10,
    #     wait_time_seconds=5
    # )
    # for msg in messages:
    #     print(f"Received: {msg['Body']}")
    #     sqs_client.delete_message(queue_url, msg['ReceiptHandle'])

    print("✅ SQS client API demonstrated")


def example_eventbridge_client():
    """Example: Use EventBridge client for event-driven workflows."""
    print("\n=== EventBridge Client ===")

    logger = get_logger("aws.eventbridge")

    # Create EventBridge client
    session = create_session(region="us-east-1")
    eventbridge_client = EventBridgeClient(session)

    # Example: Put event
    event_bus_name = "sipap-events"
    event = {
        "Source": "sipap.matches",
        "DetailType": "Match Completed",
        "Detail": safe_json_dumps({
            "match_id": "match-12345",
            "home_team": "Arsenal",
            "away_team": "Chelsea",
            "final_score": {
                "home": 2,
                "away": 1
            },
            "completed_at": current_timestamp()
        }),
        "EventBusName": event_bus_name
    }

    logger.info("Would put EventBridge event", event_bus=event_bus_name)
    print(f"Event Bus: {event_bus_name}")
    print(f"Source: {event['Source']}")
    print(f"Detail Type: {event['DetailType']}")

    # API pattern:
    # response = eventbridge_client.put_events([event])
    # print(f"Event ID: {response['Entries'][0]['EventId']}")

    print("✅ EventBridge client API demonstrated")


def example_s3_client():
    """Example: Use S3 client for object storage."""
    print("\n=== S3 Client ===")

    logger = get_logger("aws.s3")

    # Create S3 client
    session = create_session(region="us-east-1")
    s3_client = S3Client(session)

    # Example: Upload object
    bucket = "sipap-predictions"
    key = f"predictions/2026/06/match-12345-{current_timestamp()}.json"
    data = {
        "match_id": "match-12345",
        "predictions": [
            {"analyst": "statistical", "home_score": 2, "away_score": 1},
            {"analyst": "ml_model", "home_score": 1, "away_score": 1},
            {"analyst": "form_based", "home_score": 3, "away_score": 0}
        ],
        "ensemble": {
            "home_score": 2,
            "away_score": 1,
            "confidence": 0.73
        },
        "created_at": current_timestamp()
    }

    logger.info("Would upload to S3", bucket=bucket, key=key)
    print(f"Bucket: {bucket}")
    print(f"Key: {key}")
    print(f"Data size: {len(safe_json_dumps(data))} bytes")

    # API pattern:
    # s3_client.put_object(
    #     bucket=bucket,
    #     key=key,
    #     body=safe_json_dumps(data),
    #     content_type="application/json"
    # )

    # Example: Get object
    # obj = s3_client.get_object(bucket=bucket, key=key)
    # content = obj['Body'].read().decode('utf-8')
    # prediction = safe_json_loads(content)
    # print(f"Retrieved prediction: {prediction['ensemble']}")

    # Example: List objects
    # objects = s3_client.list_objects(
    #     bucket=bucket,
    #     prefix="predictions/2026/06/"
    # )
    # for obj in objects:
    #     print(f"  {obj['Key']} ({obj['Size']} bytes)")

    print("✅ S3 client API demonstrated")


def example_error_handling():
    """Example: Handle AWS service errors gracefully."""
    print("\n=== AWS Error Handling ===")

    logger = get_logger("aws.errors")

    try:
        # Simulate AWS service error
        raise AWSServiceError("Lambda function throttled: Rate exceeded")
    except AWSServiceError as e:
        logger.error("AWS service error", error=str(e))
        print(f"Caught AWSServiceError: {e}")
        print("Would implement exponential backoff retry")

    print("✅ Error handling demonstrated")


def example_cross_service_workflow():
    """Example: Workflow using multiple AWS services."""
    print("\n=== Cross-Service Workflow ===")

    logger = get_logger("aws.workflow")

    # Scenario: Process match prediction
    # 1. Receive message from SQS
    # 2. Invoke Lambda to generate prediction
    # 3. Store result in S3
    # 4. Publish event to EventBridge

    match_id = "match-99999"

    logger.info("Starting cross-service workflow", match_id=match_id)

    # Step 1: Receive from SQS (simulated)
    print("\n1. Receive match request from SQS")
    print(f"   Match ID: {match_id}")

    # Step 2: Invoke Lambda (simulated)
    print("\n2. Invoke prediction Lambda")
    prediction_result = {
        "match_id": match_id,
        "ensemble_prediction": {"home": 2, "away": 1},
        "confidence": 0.78,
        "timestamp": current_timestamp()
    }
    print(f"   Prediction: {prediction_result['ensemble_prediction']}")
    print(f"   Confidence: {prediction_result['confidence']}")

    # Step 3: Store in S3 (simulated)
    print("\n3. Store prediction in S3")
    s3_key = f"predictions/{match_id}/{current_timestamp()}.json"
    print(f"   S3 Key: {s3_key}")

    # Step 4: Publish event (simulated)
    print("\n4. Publish completion event to EventBridge")
    event_detail = {
        "match_id": match_id,
        "prediction_stored": True,
        "s3_location": s3_key
    }
    print(f"   Event Detail: {safe_json_dumps(event_detail, pretty=True)}")

    logger.info("Workflow completed", match_id=match_id)
    print("\n✅ Cross-service workflow demonstrated")


def main():
    """Run all AWS integration examples."""
    print("=" * 60)
    print("SIPAP Common - AWS Integration Examples")
    print("=" * 60)

    setup_logging()

    example_session_management()
    example_lambda_client()
    example_sqs_client()
    example_eventbridge_client()
    example_s3_client()
    example_error_handling()
    example_cross_service_workflow()

    print("\n" + "=" * 60)
    print("✅ All AWS integration examples completed!")
    print("\nKey Features:")
    print("  - Unified session management")
    print("  - Typed client wrappers (Lambda, SQS, EventBridge, S3)")
    print("  - Automatic JSON serialization")
    print("  - Structured logging for all operations")
    print("  - Consistent error handling")
    print("  - Cross-service workflow orchestration")
    print("\nTesting:")
    print("  - Use moto for AWS service mocking")
    print("  - All clients support dependency injection")
    print("  - Session isolation for parallel tests")
    print("=" * 60)


if __name__ == "__main__":
    main()
