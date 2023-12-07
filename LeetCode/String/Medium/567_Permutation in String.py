"""
https://leetcode.com/problems/permutation-in-string/
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # approach: sliding window
        if len(s1) > len(s2):
            return False
        s1_occurrences = [0] * 26
        window = [0] * 26

        k = len(s1)
        for i in range(k):
            s1_occurrences[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        count = 0
        for i in range(26):
            if s1_occurrences[i] == window[i]:
                count += 1

        for i in range(len(s2) - len(s1)):
            if count == 26:
                return True
            # add the next letter, to move the window forward
            window[ord(s2[i + len(s1)]) - ord('a')] += 1
            if s1_occurrences[i] == window[i]:
                count += 1
            elif window[i] == s1_occurrences[i] + 1:
                count -= 1
            window[ord(s2[i]) - ord('a')] -= 1
            if window[i] == s1_occurrences[i]:
                count += 1
            elif window[i] == s1_occurrences[i] - 1:
                count -= 1

        return count == 26
