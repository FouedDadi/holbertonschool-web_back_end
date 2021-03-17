#!/usr/bin/env python3
"""[collect 10 random numbers then return the 10 random numbers]"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """[async_generator]

    Returns:
        List[float]: [description]
    """
    return [x async for x in async_generator()]
