"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
"""
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 60
        res = 0
        for t in time:
            num_mod = t%60
            res += c[-num_mod]
            c[num_mod] += 1
        return res