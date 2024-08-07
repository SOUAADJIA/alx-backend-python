#!/usr/bin/env python3
"""
module for task 2
"""
from time import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension four times
    in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start = time()

    await gather(*(async_comprehension() for _ in range(4)))
    return time() - start
