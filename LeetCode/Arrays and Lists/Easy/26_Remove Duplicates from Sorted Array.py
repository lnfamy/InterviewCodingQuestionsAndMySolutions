"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


class Solution:
    """
    the array is sorted in a non decreasing order, we'll use that to our advantage
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        uniques = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[uniques] = nums[i]
                uniques += 1
            i += 1
        return uniques
