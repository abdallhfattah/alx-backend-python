#!/usr/bin/env python3
"""
    Basic annotations for variables.
"""
from typing import List, Union


def sum_mixed_list(a: List[Union[int, float]]) -> float:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """
    return sum(a)
