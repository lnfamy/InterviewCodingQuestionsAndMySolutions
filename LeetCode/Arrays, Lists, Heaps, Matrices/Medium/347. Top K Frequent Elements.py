"""
https://leetcode.com/problems/top-k-frequent-elements/description/
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # making a frequency dictionary
        freq = dict.fromkeys(nums, 0)
        for num in nums:
            freq[num] += 1

        res = []
        # sort dictionary by value descending, iterate over keys after sort
        for ky in sorted(freq, key=freq.get, reverse=True):
            # make sure we only return the k most freq. elements
            if k <= 0:
                break
            res.append(ky)
            k -= 1

        return res
