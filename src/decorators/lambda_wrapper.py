from functools import wraps

from src.decorators.json_body import json_body
from src.decorators.error_handler import error_handler


def lambda_wrapper(func):
    @wraps(func)
    @error_handler
    @json_body
    def wrapper(event, context):
        return func(event, context)
    return wrapper