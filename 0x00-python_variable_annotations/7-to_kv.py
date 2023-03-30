#!/usr/bin/env python3
"""type-annotated function to_kv that takes in complex types
and return a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, v ** 2
