"""
https://leetcode.com/problems/stickers-to-spell-word/description/
"""
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        res = self.dfs(stickers, target, 0, {})
        return res if res != float('inf') else -1

    def dfs(self, stickers, target, idx, memo):
        # if target is empty, we don't need any more stickers
        if target == "":
            return 0

        # if we've searched through all stickers, and haven't completed the target yet
        # that means that there's no solution
        if idx == len(stickers):
            return float('inf')

        # check if answer is in cache
        key = (idx, target)
        if key in memo:
            return memo[key]

        """
        the main idea is that at each point in time we have two options:
            1. take this current sticker
                we take this curren't sticker and remove all matching letters from the target
                string. we then recurse with the same list of stickers (keep idx the same)
                and add 1 to the result.
                we only stop trying to take the current sticker when it doesn't contain
                any letters in the target string
            2. don't take this current sticker.
                in this case, we increment idx by 1 and target remains the same
                as in we're jumping to the next sticker, and we have not found any new letters
            in the end, we return the minimum of the diff choices we made.
            if there's no solution, the dfs function retrns inf.
        """
        # don't take the current sticker
        res = self.dfs(stickers, target, idx + 1, memo)

        # choice 2 - take the current sticker
        curr = stickers[idx]
        new_tar = target
        removed = False
        for c in curr:
            idx_to_rm = new_tar.find(c)
            if idx_to_rm != -1:
                new_tar = new_tar[:idx_to_rm] + new_tar[idx_to_rm + 1:]
                removed = True

        if removed:
            res = min(res, 1 + self.dfs(stickers, new_tar, idx, memo))

        # cache result
        memo[key] = res
        return res