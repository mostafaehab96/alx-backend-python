#!/usr/bin/env python3
"""Waiting for a random time"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number to execute and return it"""
    waiting_time = random.uniform(0, max_delay)
    await asyncio.sleep(waiting_time)
    return waiting_time
