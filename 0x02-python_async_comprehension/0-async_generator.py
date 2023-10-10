#!/usr/bin/env python3

"""A synchronous random generator"""
import random
import asyncio


async def async_generator():
    """Creates a 10 random numbers generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
