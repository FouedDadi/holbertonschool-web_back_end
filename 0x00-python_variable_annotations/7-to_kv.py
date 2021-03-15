#!/usr/bin/env python3
"""[takes an str k and int/float v and return the k and square of v]"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """[type-annotated function]

    Args:
        k (str): [argument as string]
        v (Union[int, float]): [ints of floats as argument]

    Returns:
        tuple[str, float]: [str k and the square of v]
    """
    return (k, v**2)
