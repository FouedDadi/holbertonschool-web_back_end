#!/usr/bin/env python3
"""[annotate a function]"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[summary]

    Args:
        lst (Iterable[Sequence]): [description]

    Returns:
        List[Tuple[Sequence, int]]: [description]
    """
    return [(i, len(i)) for i in lst]
