#!/usr/bin/env python3
from typing import List, Union
import math

"""
    Basic annotations for variables.
"""


def to_kv(a : str , b : Union[float , int]) -> tuple:
    """
    Takes a list input_list of floats as argument
    returns their sum as a float.
    """
    return (a , math.pow(b , 2))
