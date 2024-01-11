#!/usr/bin/env python3
"""
type-annotated function to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple with the string k and the square of the int/float v."""
    return (k, v ** 2.0)
