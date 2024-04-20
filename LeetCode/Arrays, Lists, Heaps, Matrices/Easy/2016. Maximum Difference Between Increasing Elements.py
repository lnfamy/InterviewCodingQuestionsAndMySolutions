"""
https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_diff = max(max_diff, nums[j] - nums[i])

        return max_diff
