"""
https://leetcode.com/problems/optimal-partition-of-string/
"""
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # approach: greedy
        seen = [-1] * 26
        count = 1
        substr_start = 0

        for i in range(len(s)):
            if seen[ord(s[i]) - ord('a')] >= substr_start:
                count += 1
                substr_start = i
            seen[ord(s[i]) - ord('a')] = i

        return count
