#!/usr/bin/python3
""" Omplements a cache that follows the FIFO principle """

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ The FIFOCACHE follows the FIFO principle and implements BaseCaching
    """

    def __init__(self):
        """ init function """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """  set a value in the cache with the associated key
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            if len(self.cache_data) == self.MAX_ITEMS:
                discarded = self.queue.popleft()
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
