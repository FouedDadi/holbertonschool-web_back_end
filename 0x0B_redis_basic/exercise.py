#!/usr/bin/env python3
"""[summary]"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional


class Cache():
    """[summary]
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
        if data is not None and fn is Not None:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            str: [description]
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """[summary]

        Args:
            data (bytes): [description]

        Returns:
            int: [description]
        """
        return int.from_bytes(data, sys.byteorder)
