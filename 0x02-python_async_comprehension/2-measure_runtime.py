#!/usr/bin/env python3
""" Mesures time"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that measures and returns the runtime of
    running 4 instances of the async_comprehension function.

    Returns:
        float: The runtime of the async_comprehension function in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
