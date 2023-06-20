#!/usr/bin/python3
""" A caching system that removes the most recently used items """

from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ Cache that implements MRU and extends BaseCache
    """

    def __init__(self):
        """ this is the constructor """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """  saves an item in cache to the specified key
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            if len(self.cache_data) == self.MAX_ITEMS:
                discarded = self.queue.pop()
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ retrieves the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
