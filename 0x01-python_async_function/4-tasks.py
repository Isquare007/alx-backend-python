#!/usr/bin/env python3
"""alter wait_n into a new function task_wait_n"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """identical to wait_n"""
    result = await asyncio.gather(*(
        task_wait_random(max_delay) for _ in range(n)))
    # return sorted(result)
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[i] > result[j]:
                temp = result[i]
                result[i] = result[j]
                result[j] = temp

    return result
