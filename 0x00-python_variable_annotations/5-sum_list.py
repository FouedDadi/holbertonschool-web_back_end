#!/usr/bin/env python3
"""[takes a list of floats and return the sum as float]"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """[type-annotated function]

    Args:
        input_list (List[float]): [list of floats as argument]

    Returns:
        float: [sum of all floats in list]
    """
    return sum(input_list)
