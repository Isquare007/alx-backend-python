#!/usr/bin/env python3
"""a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure_runtime should measure the total runtime
    of 4 async comprehension and return it."""
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
