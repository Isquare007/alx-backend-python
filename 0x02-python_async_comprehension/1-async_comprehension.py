#!/usr/bin/env python3
"""async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments."""
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """using an async comprehensing over async_generator,
    then return the 10 random numbers"""
    return [x async for x in async_generator()]
