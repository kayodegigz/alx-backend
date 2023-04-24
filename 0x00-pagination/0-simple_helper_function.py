#!/usr/bin/env python3
"""
Index range
"""


def index_range(page, page_size):
    """
    Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list.
    """
    tup = ((page - 1) * page_size, page * page_size)
    return tup
