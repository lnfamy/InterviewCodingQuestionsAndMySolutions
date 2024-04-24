"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
"""
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(weight_cap):
            days_taken = 1
            curr = 0
            for w in weights:
                curr += w
                if curr > weight_cap:
                    days_taken += 1
                    curr = w

            return days_taken <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            days_for_mid_capacity = possible(mid)
            if days_for_mid_capacity:
                right = mid
            else:
                left = mid + 1

        return left