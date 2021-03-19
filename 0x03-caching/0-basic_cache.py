#!/usr/bin/python3
"""Create a class BasicCache that inherits from BaseCaching"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """[class BasicCache]

    Args:
        BaseCaching ([type]): [description]
    """
    def put(self, key, item):
        """[put]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """[get]

        Args:
            key ([type]): [description]
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
