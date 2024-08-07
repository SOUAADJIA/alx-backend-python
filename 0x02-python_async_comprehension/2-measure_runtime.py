#!/usr/bin/env python3
"""
Module for task 2: Measure runtime for four parallel comprehensions
"""
from time import time
from asyncio import gather
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension four times
    in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start = time()

    # Run async_comprehension 4 times in parallel using gather
    await gather(*(async_comprehension() for _ in range(4)))

    total_runtime = time() - start
    return total_runtime
