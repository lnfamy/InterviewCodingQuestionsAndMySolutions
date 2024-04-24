"""
https://leetcode.com/problems/word-break/description/

alternative wording:
kitty in horror house
a kitty is locked inside of a horror house. there are distinct random words written on the wall.
kitty met a ghost inside the house. ghost offered to help, but on one condition. he said "i will give you a word.
you need to tell if you can create this word using the words written on the walls of the horror house. if you are
correct, ill take you out of the house. else, you are stuck here forever". you need to write an algorithm which can
help the kitty. you need to return true if it's possible, false otherwise.
note: the same word in the dictionary can be reused multiple times in the segmentation if you need.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        # dp 0 is true because a string of length 0 can be made by doing nothing with wordDict, still legal
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
