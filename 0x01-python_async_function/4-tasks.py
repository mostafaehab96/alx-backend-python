#!/usr/bin/env python3
"""Creating multiple coroutines"""

import asyncio
import bisect
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait, execute then returns a list of waiting!"""
    waitings = []
    for i in range(n):
        wait_time = await task_wait_random(max_delay)
        bisect.insort_left(waitings, wait_time)

    return waitings
