#!/usr/bin/env python3
"""measure runtime"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measuring time of wait_n function"""
    total_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = (time.time() - total_time) / n
    return total_time
