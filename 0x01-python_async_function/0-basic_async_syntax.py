#!/usr/bin/env python3
"""[asynchronous coroutine that takes in an int and awaits for random delay]"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[asynchronous coroutine]

    Args:
        max_delay (int, optional): [arg]. Defaults to 10.

    Returns:
        float: [random await]
    """
    randomised: float = random.uniform(0, max_delay)
    await asyncio.sleep(randomised)
    return randomised
