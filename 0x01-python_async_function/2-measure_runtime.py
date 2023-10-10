#!/usr/bin/env python3
"""Measuring execution time."""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns the time of execution"""
    now = time.time()
    task = asyncio.create_task(wait_n(n, max_delay))
    await task
    return time.time() - now
