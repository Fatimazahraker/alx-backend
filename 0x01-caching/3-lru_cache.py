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
        """ Add an item in the cache (LRU algorithm) """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.order.append(key)
    
    def get(self, key):
        """ Get an item by key (LRU algorithm) """
        if key is not None and key in self.cache_data:
            # Move the accessed key to the end of the order to mark it as most recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
