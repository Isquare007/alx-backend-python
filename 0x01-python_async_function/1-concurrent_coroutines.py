#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay"""

    result = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    # return sorted(result)
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[i] > result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result
