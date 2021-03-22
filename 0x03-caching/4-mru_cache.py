#!/usr/bin/python3
"""Create a class MRUCache that inherits from BaseCaching"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """[class MRUCache]

    Args:
        BaseCaching ([type]): [description]
    """
    _cache = []

    def put(self, key, item):
        """[put method]

        Args:
            key ([type]): [description]
            item ([type]): [description]
        """

        if key and item:
            self.cache_data[key] = item
            if key not in self._cache:
                self._cache.append(key)
            else:
                self._cache.append(self._cache.pop(self._cache.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                deleted = self._cache.pop(-2)
                del self.cache_data[deleted]
                print("DISCARD: {}".format(deleted))

    def get(self, key):
        """[get method]

        Args:
            key ([type]): [description]
        """
        if key and self.cache_data.get(key):
            self._cache.append(self._cache.pop(self._cache.index(key)))
            return self.cache_data.get(key)
