#!/usr/bin/env python3
from typing import List, Union , Tuple
import math

"""
    Basic annotations for variables.
"""


def to_kv(a : str , b : Union[float , int]) -> Tuple[str, float]:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """
    return (a , math.pow(b , 2))
