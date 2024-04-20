"""
https://leetcode.com/problems/beautiful-arrangement/description/
"""
from typing import List


class Solution:
    def __init__(self):
        self.ans = None

    def countArrangement(self, n: int) -> int:
        self.ans = 0
        nums = [i for i in range(1, n + 1)]

        def dfs(nums: List, i: int = 1):
            if i == n + 1:
                # if we got here, that means we got through a whole permutation.
                # this means we can increment the answer (number of beautiful arrangements)
                self.ans += 1
                return
            for j, num in enumerate(nums):
                # explanation: if num % i AND i % num - we fulfill both conditions, which is something
                # that we don't want. we want exactly one of the conditions to be fulfilled at any given time.
                # therefore, we check: if the number is divisible by i OR i is divisible by the number
                # and if that's true, this number can remain in this placement for this permutation and we 
                # remove the number from nums and continue generating the permutation.
                if not (num % i and i % num):
                    dfs(nums[:j] + nums[j + 1:], i + 1)

        dfs(nums)
        return self.ans

