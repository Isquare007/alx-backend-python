#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """The function takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay"""

    wait_time = uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
