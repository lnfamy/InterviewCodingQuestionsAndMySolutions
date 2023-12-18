"""
https://leetcode.com/problems/longest-arithmetic-subsequence/description/
"""


class Solution:
    # approach: dynamic programming
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # 2d array dp[a][b] for dynamic programming, saves the length of the longest arithmetic sequence
        # that ends with the element at index [a] with a common difference of [b]
        dp = {}

        # we iterate over every last index 'right'
        # and for every 'right' index, we iterate over the second-to-last index 'left', from 0 to right - 1

        for right in range(len(nums)):
            for left in range(0, right):
                # now we check if we can 'elongate' this sequence from the left, ie. we check
                # if there's anything to the left of 'right' that maintains that same common difference
                # if so, we add +1 to the entry that ends at right, with the common difference calculated
                diff = nums[right] - nums[left]
                # equal to java's getOrDefault method. if no such sequence exists, this is the first
                # time we note it down and therefore we get the default value, which we have to increment
                # by 1 to reflect the length of a 2-element sequence (2)
                # if it does exist, then we do find the length of the existing sequence and add 1 onto it
                # to reflect the addition of the new element to it
                dp[(right, diff)] = dp.get((left, diff), 1) + 1

        return max(dp.values())
