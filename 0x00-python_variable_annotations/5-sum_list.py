#!/usr/bin/env python3
"""type-annotated function sum_list which takes a list input_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum up the float value of a list"""
    sumup = 0
    for x in input_list:
        sumup = sumup + x

    return sumup
