#!/usr/bin/env python3
from typing import Union, Tuple

"""
    Basic annotations for variables.
"""


def to_kv(k: str, b: Union[float, int]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments
    returns a tuple.
    """
    return (k, b**2)
