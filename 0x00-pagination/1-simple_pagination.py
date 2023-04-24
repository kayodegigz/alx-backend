#!/usr/bin/env python3
"""
Server Class
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list.
    """
    tup = ((page - 1) * page_size, page * page_size)
    return tup

class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        The dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page that takes two integer arguments; page 
        and page_size with default values 1 and 10
        this function uses index_range to find the correct index to paginate
        the dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
