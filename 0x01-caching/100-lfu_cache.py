#!/usr/bin/python3
""" A caching system that removes the least recently used items """

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ Cache that implements LRU and extends BaseCache
    """

    def __init__(self):
        """ this is the constructor """
        super().__init__()
        self.obj = {}

    def put(self, key, item):
        """  saves an item in cache to the specified key
        """
        if key and item:
            if (len(self.cache_data) == self.MAX_ITEMS
                    and key not in self.cache_data):
                discarded = min(self.obj, key=self.obj.get)
                del self.cache_data[discarded]
                del self.obj[discarded]
                print("DISCARD: {}".format(discarded))

            if key in self.cache_data:
                self.obj[key] += 1
            else:
                self.obj[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """ retrieves the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.obj[key] += 1
            return self.cache_data.get(key)
