#!/usr/bin/env python3
"""
Module for task 1 - Concurrent Coroutines
"""
from asyncio import gather
from typing import List
from random import uniform
from time import sleep

async def wait_random(max_delay: int) -> float:
    """
    Asynchronously wait for a random delay and return it.

    Args:
        max_delay (int): Maximum delay time in seconds.

    Returns:
        float: The actual delay time.
    """
    delay = uniform(0, max_delay)
    sleep(delay)
    return delay

async def wait_n(num_times: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random num_times times with the specified max_delay.

    Args:
        num_times (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay time in seconds.

    Returns:
        List[float]: List of all the delays (float values) sorted.
    """
    return sorted(
        await gather(
            *[wait_random(max_delay) for _ in range(num_times)]
        )
    )
