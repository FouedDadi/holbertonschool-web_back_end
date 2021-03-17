#!/usr/bin/env python3
"""[collect 10 random numbers then return the 10 random numbers]"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """[measure_runtime]

    Returns:
        float: [total time]
    """
    tasks = []
    start = time.time()
    for x in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end = time.time()
    total = end - start
    return total
