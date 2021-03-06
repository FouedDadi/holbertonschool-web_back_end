#!/usr/bin/env python3
"""[loop 10 times then yield a random number between 0 and 10]"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """[async_generator]

    Yields:
        Generator[float, None, None]: []
    """
    for value in range(10):
        await asyncio.sleep(1)
        value = random.random() * 10
        yield value
