#!/usr/bin/env python3
"""[]"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """[summary]

    Args:
        k (str): [argument as string]
        v (Union[int, float]): [ints of floats as argument]

    Returns:
        tuple[str, float]: [str k and the square of v]
    """
    return (k, v**2)
