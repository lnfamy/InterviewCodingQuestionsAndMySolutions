"""
https://leetcode.com/problems/get-equal-substrings-within-budget/
"""
class Solution:
    # naive approach. correct, but gives TLE
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        mx_count = 0

        def max_for_index(k):
            lcl_cost = 0
            lcl_count = 0
            for i in range(k, len(s)):
                curr = abs(ord(s[i]) - ord(t[i]))
                if lcl_cost + curr > maxCost:
                    return lcl_count
                lcl_cost += curr
                lcl_count += 1
            return lcl_count

        for i in range(len(s)):
            res = max_for_index(i)
            mx_count = max(mx_count, res)

        return mx_count

    # sliding window approach
    def equalSubstring_v2(self, s: str, t: str, maxCost: int) -> int:
        j = 0
        for i in range(len(s)):
            maxCost -= abs(ord(s[i]) - ord(t[i]))
            if maxCost < 0:
                maxCost += abs(ord(s[j]) - ord(t[j]))
                j += 1

        return i - j + 1

