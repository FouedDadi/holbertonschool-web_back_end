#!/usr/bin/env python3
"""[float as arg and returns a function (multiplies a float by multiplier)]"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[type-annotated function]

    Args:
        multiplier (float): [argument float]

    Returns:
        callable[[float], float]: [funct that multiplies float by multiplier]
    """
    return lambda y: y * multiplier
