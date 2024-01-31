#!/usr/bin/env python3
"""A script for caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """
    def __init__(self):
        """initialize BasicCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign to the dictionary
        self.cache_data the item value for the key key
        """
        if key is None or item is None:
            return
        capacity = len(self.cache_data)
        if capacity >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order[0]
            del self.cache_data[discarded_key]
            self.order.pop(0)
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key

        Args:
            key (_type_): _description_
        """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
