#!/usr/bin/env python3
"""
module for task 2
"""

import asyncio
import time
from typing import List
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.

    Returns:
        float: Total runtime for executing the four coroutines.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in four_copies))
    end_time = time.perf_counter()
    return end_time - start_time
