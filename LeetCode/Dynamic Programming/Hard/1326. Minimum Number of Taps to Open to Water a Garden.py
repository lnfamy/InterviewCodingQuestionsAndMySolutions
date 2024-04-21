"""
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/
"""
from typing import List


class Solution:
    """
    approach 1: dynamic programming
    not the best runtime, but good memory usage
    """
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            for j in range(start, end):
                if (dp[j] + 1) < dp[end]:
                    dp[end] = dp[j] + 1

        if dp[n] == float('inf'):
            return -1

        return dp[n]

"""
approach 2:
greedy. better runtime, around the same usage of memory as first
"""


class Solution2:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)

        # calculate max reach for each tap
        for i in range(len(ranges)):
            # leftmost position
            start = max(0, i - ranges[i])
            # rightmost position
            end = min(n, i + ranges[i])

            # update max reach for leftmost position
            max_reach[start] = max(max_reach[start], end)

        # initialize number of taps used
        taps = 0
        # current rightmost position reached
        curr_end = 0
        # next rightmost position that can be reached
        next_end = 0

        # iterating through the garden
        for i in range(n + 1):
            if i > next_end:
                # then the current position cannot be reached
                return -1

            if i > curr_end:
                taps += 1
                curr_end = next_end

            next_end = max(next_end, max_reach[i])
        return taps