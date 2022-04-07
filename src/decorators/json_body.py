import json

from functools import wraps


def json_body(func):
    @wraps(func)
    def wrapper(event, context):
        if 'body' in event:
            event['body'] = json.loads(event['body'])
        return func(event, context)
    return wrapper
