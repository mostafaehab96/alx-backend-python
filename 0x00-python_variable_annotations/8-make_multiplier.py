#!/usr/bin/env python3

"""Defines make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that accepts a float and multiply
    it by multiplier parameter
    """

    def multiply(n: float):
        return n * multiplier

    return multiply
