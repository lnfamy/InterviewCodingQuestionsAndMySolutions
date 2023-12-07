"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/description/
"""


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # last approach to solve: binary search
        length = len(nums)
        nums_range = 100

        left = 1
        right = length * nums_range

        while left < right:
            mid = (left + right) // 2
            total = mid
            valid = True

            for num in nums:
                total += num
                if total < 1:
                    valid = False
                    break
            # if valid, that means that the value we need is lower than mid
            # regardless, this part reduces the search by half
            if valid:
                right = mid
            else:
                left = mid + 1

        return left
