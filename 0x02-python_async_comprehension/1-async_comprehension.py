#!/usr/bin/env python3
"""Creating async comprehension"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing over async_generator
    :return: the 10 random numbers.
    """
    numbers = [i async for i in async_generator()]
    return numbers
