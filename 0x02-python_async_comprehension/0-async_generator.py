#!/usr/bin/env python3
"""async generatro"""
import asyncio
import random


async def async_generator():
    """async generatorr"""
    for _ in range(11):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
