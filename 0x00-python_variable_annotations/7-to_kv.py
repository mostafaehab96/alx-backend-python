#!/usr/bin/env python3
"""Defines to_kv function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of string k and square of v"""
    return (k, v ** 2)
