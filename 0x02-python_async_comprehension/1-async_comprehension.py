#!/usr/bin/env python3
"""
module for task 1
"""

from typing import List
async_generator = __import__('async_generator_module').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine will collect 10 random numbers
    using an async comprehension over async_generator.
    """
    return [number async for number in async_generator()]
