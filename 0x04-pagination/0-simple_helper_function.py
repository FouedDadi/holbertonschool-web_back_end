#!/usr/bin/env python3
"""function index_range that takes two integer arguments page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[index range]

    Args:
        page (int): [arg 1]
        page_size (int): [arg 2]

    Returns:
        Tuple[int, int]: [return start index and end index]
    """
    return (page - 1) * page_size, page * page_size
