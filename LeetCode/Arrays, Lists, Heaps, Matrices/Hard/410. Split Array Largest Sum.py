"""
https://leetcode.com/problems/split-array-largest-sum/description/
"""
from typing import List


class Solution:
    """
    approach: binary search
    """

    def splitArray(self, nums: List[int], k: int) -> int:

        def min_subarrays_req(max_sum: int) -> int:
            cur = 0
            splits_req = 0

            for num in nums:
                if cur + num <= max_allowed:
                    cur += num
                else:
                    splits_req += 1
                    cur = num

            return splits_req + 1

        sum_elem = sum(nums)
        max_elem = max(nums)
        res = sum_elem
        """
        so we know that the smallest possible subarray sum is, ideally - equal to the
        value of the largest element in the original array. and continuing off of this logic,
        the largest possible subarray sum is the sum of all elements (relevant in the case
        where k == 1). therefore we set the initial boundaries of the binary search to be:
            1. left - max_elem
            2. right - sum_elem
        """
        left = max_elem
        right = sum_elem

        while not left > right:
            # max subarray sum allowed
            max_allowed = (left + right) // 2

            splits_required = min_subarrays_req(max_allowed)
            if splits_required <= k:
                res = max_allowed
                right = max_allowed - 1
            else:
                left = max_allowed + 1

        return res