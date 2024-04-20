"""
https://leetcode.com/problems/lfu-cache/description/
"""
import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # cache: key -> [val, freq]
        self.cache = dict()
        # count -> ordered dict (key -> None)
        # ordered dict remembers the order in which items were inserted
        self.cache_freqs = dict()
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, old_freq = self.cache[key]
        self.cache[key][1] += 1
        self.cache_freqs[old_freq].pop(key)
        self.update_cache_freqs(key, old_freq + 1)

        # if old freq was the prev min and there exists no more cache
        # items for that minimum, then increment
        if old_freq == self.min_freq and len(self.cache_freqs[old_freq]) == 0:
            self.min_freq = old_freq + 1

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            # reuse get() method to update the count of the key
            _ = self.get(key)
            self.cache[key][0] = value
            return

        # if we need to make room in the cache
        if len(self.cache) == self.capacity:
            remove, _ = self.cache_freqs[self.min_freq].popitem(False)
            self.cache.pop(remove)

        # now to insert into the cache
        self.cache[key] = [value, 1]
        self.update_cache_freqs(key, 1)
        self.min_freq = 1

    def update_cache_freqs(self, key: int, freq: int):
        # first occurence of freq
        if freq not in self.cache_freqs:
            self.cache_freqs[freq] = collections.OrderedDict()

        # add to freqs
        self.cache_freqs[freq][key] = None

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)