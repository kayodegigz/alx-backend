#!/usr/bin/python3
""" Implementing a simple cache """


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching parent class """

    def put(self, key, item):
        """Sets an item to the specified key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves data from the dict that's associated with a key """
        return self.cache_data.get(key, None)