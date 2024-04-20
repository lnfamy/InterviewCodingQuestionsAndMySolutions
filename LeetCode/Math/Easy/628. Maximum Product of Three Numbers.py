"""
https://leetcode.com/problems/maximum-product-of-three-numbers/description/
constraints:
nums length between 3 and 10^4
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        nums.sort()
        # last element in second option is nums[-1] to account for two big negative numbers edge case
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])