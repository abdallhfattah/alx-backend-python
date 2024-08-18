#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument,
    returns a function that multiplies a float by multiplier.
    """

    def fun(n: float) -> float:
        "multiplies a float by multiplier"
        return n * multiplier

    return fun
