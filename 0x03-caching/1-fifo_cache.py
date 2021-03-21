#!/usr/bin/python3
"""Create a class FIFOCache that inherits from BaseCaching"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """[class FIFOCache]

    Args:
        BaseCaching ([type]): [description]
    """
    def put(self, key, item):
        """[put method]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            deleted = self.cache_data
            dlt = list(deleted).pop(0)
            del self.cache_data[dlt]
            print("DISCARD: {}".format(dlt))

    def get(self, key):
        """[get method]

        Args:
            key ([type]): [description]
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
