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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        get_hyper that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page: the current page
        number data: the dataset (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        st, ed = index_range(page, page_size)
        data = self.dataset()[st:ed]
        total_pgs = math.ceil(len(self.dataset()) / page_size)
        if page >= total_pgs:
            next_pg = None
        else:
            next_pg = page + 1
        if page <= 1:
            prev_pg = None
        else:
            prev_pg = page - 1

        return {
                "page_size": page_size,
                "page": page, "data": data,
                "next_page": next_pg,
                "prev_page": prev_pg,
                "total_pages": total_pgs}
