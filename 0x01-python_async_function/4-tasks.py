#!/usr/bin/env python3
"""[spawn wait_random n times with the specified max_delay]"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """[execute multiple coroutines]

    Args:
        n (int): [arg1]
        max_delay (int, optional): [arg2]. Defaults to 10.

    Returns:
        List[float]: [all delays (list of floats)]
    """
    spawns = []
    delays = []
    for x in range(n):
        spawns.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(spawns):
        delays.append(await task)
    return delays
