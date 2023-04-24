#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index return a dictionary containing the following key-value pairs:
        index: the current start index of the return page
        page_size: the current page size
        data: the dataset page (equivalent to return from previous task)
        next_index: the next index to query with, None if no next page
        prev_index: the previous index to query with, None if no previous
        page
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        data = []
        next_index = None
        prev_index = None
        dataset = self.indexed_dataset()
        for i in range(index, index + page_size):
            if i in dataset:
                data.append(dataset[i])
            else:
                break

            if index + page_size in dataset:
                next_index = index + page_size
            if index - page_size >= 0:
                prev_index = index - page_size
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
