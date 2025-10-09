from typing import List, Union
from logtail import LogtailHandler
import logging

SOURCE_TOKEN = "1v34p6t5z7sB5aVQBgxBhHYg"
HOST = "s1523202.eu-nbg-2.betterstackdata.com"


def get_logger():
    handler = LogtailHandler(
        source_token=SOURCE_TOKEN,
        host=f'https://{HOST}',
    )
    logger = logging.getLogger("buddylogger")
    logger.setLevel(logging.INFO)
    logger.handlers = []
    logger.addHandler(handler)
    return logger


logger = get_logger()


def say_hello() -> str:
    result = "Hello, buddy"
    logger.info(f"Function say_hello called → result: {result}")
    return result


def get_max_number(numbers: List[Union[int, float]]) -> Union[int, float]:
    valid_numbers = [n for n in numbers if isinstance(n, (int, float))]
    result = max(valid_numbers) if valid_numbers else 0
    logger.info(f"Function get_max_number called with {numbers} → result: {result}")
    return result


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    result = a * b
    logger.info(f"Function multiply called with a={a}, b={b} → result: {result}")
    return result