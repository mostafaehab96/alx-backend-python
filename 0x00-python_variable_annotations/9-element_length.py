#!/usr/bin/env python3
"""Defines element_length function"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    :param lst: a list of any sequences
    :return: a list of tuples where each tuple contains the sequence and
    it's length
    """
    return [(i, len(i)) for i in lst]
