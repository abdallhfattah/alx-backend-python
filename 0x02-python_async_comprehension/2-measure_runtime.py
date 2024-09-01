#!/usr/bin/env python3
""" documenting """
import typing
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measuring run time of async comprehension function"""

    start = time.time()
    asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.time() - start
