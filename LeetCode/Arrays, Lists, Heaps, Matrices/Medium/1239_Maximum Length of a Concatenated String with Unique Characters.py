"""
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
"""


class Solution:
    # approach: recursion
    def recurse(self, words, index, word):
        if len(word) != len(set(word)):
            return
        self.answer = max(self.answer, len(word))
        if index == len(words):
            return
        for i in range(index, len(words)):
            self.recurse(words, i + 1, word + words[i])

    def maxLength_recurse(self, arr: List[str]) -> int:
        self.answer = 0
        self.recurse(arr, 0, "")
        return self.answer

    # approach: backtracking (using dfs)
    def maxLength_backtracking(self, arr: List[str]) -> int:
        self.answer = 0
        self.recurse(arr, 0, "")
        return self.answer

    class Solution:
        # approach: iterative
        def maxLength_iterative(self, arr: List[str]) -> int:
            concat = [""]
            longest = 0
            for letters in arr:
                for i in range(len(concat)):
                    new_result = concat[i] + letters
                    if len(new_result) == len(set(new_result)):
                        concat.append(new_result)
                        longest = max(longest, len(new_result))
            return longest
