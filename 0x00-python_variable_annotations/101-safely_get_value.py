#!/usr/bin/env python3

"""Add type annotation to the function below"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[Any, T]:
    """Returns a value in dictionary dict if key is available else returns a
    default value or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
