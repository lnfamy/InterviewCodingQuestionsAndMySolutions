"""
https://leetcode.com/problems/rotate-array/
"""
class Solution(object):
    # approach: reverse
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    def rotate_cyclic(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        approach: cyclic replacement
        """
        k = k % len(nums)
        start = count = 0
        while count < len(nums):
            curr = start
            prev = nums[start]
            while True:
                next_index = (curr + k) % len(nums)
                nums[next_index], prev = prev, nums[next_index]
                curr = next_index
                count += 1

                if start == curr:
                    break
            start += 1


