#!/usr/bin/env python3
"""[summary]"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """[summary]

        Args:
            method ([type]): [description]

        Returns:
            [type]: [description]
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """[summary]

    Args:
        method (Callable): [description]

    Returns:
        Callable: [description]
    """
    key = method.__qualname__
    inp = "".join([key, ":inputs"])
    out = "".join([key, ":outputs"])

    @wraps(method)
    def wrapper(self, *args):
        """[summary]

        Args:
            method ([type]): [description]

        Returns:
            [type]: [description]
        """
        self._redis.rpush(inp, str(args))
        self._redis.rpush(out, str(method(self, *args)))
        return method(self, *args)
    return wrapper


class Cache():
    """[summary]
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """[summary]

        Args:
            data (Union[str, bytes, int, float]): [description]

        Returns:
            str: [description]
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """[summary]
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            str: [description]
        """
        return data.decode()

    def get_int(self, data: bytes) -> int:
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            int: [description]
        """
        return int(data)
