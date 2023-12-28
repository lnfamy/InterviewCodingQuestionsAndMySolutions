"""
https://leetcode.com/problems/find-missing-observations/description/
"""


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_m = sum(rolls)

        sum_missing = mean * (m + n) - sum_m
        # if we have too many rolls to stay within the constraint of
        # missing_sum
        # OR if we can't get to sum_missing in n rolls
        if sum_missing > 6 * n or sum_missing < n:
            return []

        # distribute the rolls between the n missing observation to generate
        # an array of size n of possible missing observations that fits the
        # requirements. using pigeonhole principle.
        missing = [0] * n
        part = sum_missing // n

        for i in range(n):
            missing[i] += part
            sum_missing -= part

        if sum_missing != 0:
            for i in range(sum_missing % n):
                missing[i] += 1

        return missing
