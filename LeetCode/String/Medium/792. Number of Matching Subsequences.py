
"""
https://leetcode.com/problems/number-of-matching-subsequences/
"""
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_substring(word):
            i = -1
            for ch in word:
                # find() receives two arguments: sub - str, and end - int - so the substring that we are to search
                # and the index from which we are to start the search. so we search from i + 1 because i is initialized
                # to -1. so to start from the beginning of the string we add 1 to make it 0.
                i = s.find(ch, i + 1)
                # if the letter doesn't exist in the string, we return false because the substring isn't there
                if i == -1:
                    return False
            return True

        ans = 0
        for word in words:
            if is_substring(word):
                ans += 1

        return ans