#!/usr/bin/env python3
"""[method get_page that takes two integer arguments page and page_size]"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """[get page]

        Args:
            page (int, optional): [arg 1]. Defaults to 1.
            page_size (int, optional): [arg 2]. Defaults to 10.

        Returns:
            List[List]: [description]
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page_size > 0
        assert page > 0
        start_idx, end_idx = index_range(page, page_size)
        if start_idx >= len(self.dataset()):
            return []
        else:
            return self.dataset()[start_idx:end_idx]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """[index range]

    Args:
        page (int): [arg 1]
        page_size (int): [arg 2]

    Returns:
        Tuple[int, int]: [return start index and end index]
    """
    return (page - 1) * page_size, page * page_size
