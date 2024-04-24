"""
https://leetcode.com/problems/predict-the-winner/description/
"""
import collections
from typing import List


class Solution:
    """
    approach: top down DP
    an intuitive solution would use recursion, with the idea of dfs in mind.
    during each turn, we calculate all encountered max_score(left, right) recursively to
    consider all possible paths.
    however, this includes a lot of redundant calculations. therefore we'll use a memo
    dictionary so as to immediately return the result of a previously calculated pair.
    """

    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = collections.defaultdict(int)

        def max_diff(left, right):
            # if we've already calculated max_diff(left, right), return the saved result
            if (left, right) in memo:
                return memo[(left, right)]
            # if indices are equal, it doesn't matter
            if left == right:
                return nums[left]
            # now we calculate the possible score in case we chose left. recurse here
            score_left = nums[left] - max_diff(left + 1, right)
            # and the possible score in case we chose right. here's the recursion
            score_right = nums[right] - max_diff(left, right - 1)

            # we save to memo the higher score of the two
            memo[(left, right)] = max(score_left, score_right)
            return memo[(left, right)]

        # calling for the recursive function
        return max_diff(0, n - 1) >= 0