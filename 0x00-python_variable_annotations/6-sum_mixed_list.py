#!/usr/bin/env python3
"""
Defines sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of mxd_list"""
    return sum(mxd_list)
