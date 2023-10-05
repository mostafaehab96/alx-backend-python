#!/usr/bin/env python3

"""Exploring annotations for this function below"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if not None else return None"""
    if lst:
        return lst[0]
    else:
        return None
