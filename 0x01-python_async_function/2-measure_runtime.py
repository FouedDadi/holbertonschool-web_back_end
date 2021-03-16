#!/usr/bin/env python3
"""[measure the total execution time for wait_n(n, max_delay)]"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[(time after execution) - (start time) / n]

    Args:
        n (int): [arg1]
        max_delay (int): [arg2]

    Returns:
        float: [total time of execution]
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time() - start
    return end / n
