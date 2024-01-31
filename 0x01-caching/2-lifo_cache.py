#!/usr/bin/env python3
"""A script for caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """
    def __init__(self):
        """initialize BasicCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put key value pair into cache"""
        if (key is None or item is None):
            return
        capacity = BaseCaching.MAX_ITEMS
        self.cache_data[key] = item
        self.order.append(key)
        # if key in self.cache_data:
        #     self.cache_data[key] = item
        if len(self.cache_data) > capacity:
            key_to_pop = self.order[-2]
            del self.cache_data[key_to_pop]
            print(f"DISCARD: {key_to_pop}")

    def get(self, key):
        """ return the value in self.cache_data linked to key

        Args:
            key (_type_): _description_
        """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
