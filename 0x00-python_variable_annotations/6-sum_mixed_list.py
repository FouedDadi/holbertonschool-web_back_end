#!/usr/bin/env python3
"""[which takes a list of ints and floats and returns their sum as a float]"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """[summary]

    Args:
        mxd_lst (List[Union[int, float]]): [list of ints and floats as arg]

    Returns:
        float: [sum of ints and floats as float]
    """
    return sum(mxd_lst)
