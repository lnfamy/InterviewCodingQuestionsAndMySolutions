"""
https://leetcode.com/problems/degree-of-an-array/description/
"""
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = dict.fromkeys(nums, 0)
        left = {}
        right = {}

        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            freq[nums[i]] += 1

        ans = len(nums)
        deg = max(freq.values())

        for f in freq:
            if freq[f] == deg:
                ans = min(ans, right[f] - left[f] + 1)

        return ans
