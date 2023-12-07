"""
https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/
"""


class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        pattern = "abc"
        k = len(word)
        i = j = 0
        counter = 0
        while i < k:
            pattern_index = j % k
            if word[i] != pattern[pattern_index]:
                str_list = list(word)
                str_list.insert(i + 1, pattern[pattern_index])
                word = ''.join(str_list)
                counter += 1
            else:
                j += 1
            i += 1
        return counter
