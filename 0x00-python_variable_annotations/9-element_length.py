#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import List, Tuple, Sequence , Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Element length """
    return [(i, len(i)) for i in lst]
