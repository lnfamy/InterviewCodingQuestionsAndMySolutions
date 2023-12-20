"""
https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
"""


class Solution:
    def reverse_st(self, ls, left, right):
        while left < right:
            ls[left], ls[right] = ls[right], ls[left]
            left, right = left + 1, right - 1

    def reverse_words(self, ls):
        n = len(ls)
        start = end = 0

        while start < n:
            while end < n and ls[end] != ' ':
                end += 1
            # now that we reached either the end of the string or a whitespace, reverse the word
            self.reverse_st(ls, start, end - 1)
            # next iteration
            start = end + 1
            end += 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse entire string in place
        self.reverse_st(s, 0, len(s) - 1)

        # reverse every single word in the string
        self.reverse_words(s)
