#!/usr/bin/env python3
"""type annotated function that floors a float"""
from math import floor as roundup


def floor(n: float) -> int:
    """floors a float"""
    return roundup(n)
