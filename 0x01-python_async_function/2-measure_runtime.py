#!/usr/bin/env python3
"""Measuring execution time."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Returns the time of execution"""
    now = time.time()
    await wait_n(n, max_delay)
    return time.time() - now
