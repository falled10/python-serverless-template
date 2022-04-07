import json

from src.decorators.lambda_wrapper import lambda_wrapper


@lambda_wrapper
def handler(event, context):
    body = {
        "message": "Hello from lambda",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
