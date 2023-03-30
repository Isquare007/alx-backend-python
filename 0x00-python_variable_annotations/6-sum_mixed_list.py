#!/usr/bin/env python3
"""type annotion for list of mixed types"""
from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return the sum of a list of int and floats"""

    return sum(mxd_list)
