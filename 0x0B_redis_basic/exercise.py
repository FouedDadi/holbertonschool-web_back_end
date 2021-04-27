#!/usr/bin/env python3
"""[summary]"""

import redis
from uuid import uuid4
from typing import Union


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
