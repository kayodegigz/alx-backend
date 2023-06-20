#!/usr/bin/python3
""" Implements a last in first out cache """


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system that extends basecache and implements LIFO principe
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """  save an item n cache to a specific key """
        if key and item:
            if key in self.stack:
                self.stack.remove(key)
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                discarded = self.stack.pop()
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
