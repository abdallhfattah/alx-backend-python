#!/usr/bin/env python3

import typing
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    start = time.time()
    waiting_list = await async_comprehension()
    return time.time() - start
