#!/usr/bin/env python3
"""a coroutine async generator"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """this function will loop 10 times each time it waits for 1 sec """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
