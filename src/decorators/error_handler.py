from functools import wraps
from pydantic import ValidationError


def error_handler(func):
    @wraps(func)
    def wrapper(event, handler):
        try:
            return func(event, handler)
        except ValidationError as e:
            return {
                "statusCode": 400,
                "body": e.json()
            }
    return wrapper
