"""
https://leetcode.com/problems/distinct-subsequences/description/
"""


class Solution:
    """
    approach: dfs + memoization (DP)
    """

    def numDistinct(self, s: str, t: str) -> int:
        # init memoization dictionary
        memo = {}

        def dfs(i, j):
            # exit condition: if we finished iterating j over to the end of t, we found a valid subsq and return 1
            if j == len(t):
                return 1
            # exit condition: if i reached the end of s but j hasn't reached the end of t, we can't form a subsq.
            if i == len(s):
                return 0
            # exit condition: if the res for the current i,j pair has already been computed,
            # return it from our memo dictionary
            if (i, j) in memo:
                return memo[(i, j)]

            # if s[i] == t[j] we have two "choices", so we run dfs twice:
            # first option is to include s[i] in the subsq and recursively explore from the next characters
            # by calling dfs with i+1, j + 1.
            # second option is to exclude s[i] from the subsq and move forward only in s by calling dfs with i + 1, j
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                # if they're not equal, we can only exclude s[i] from the subsq and move forward in s only
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i, j)]

        # start the search from the initial positions at strings s and t, 0 and 0.
        return dfs(0, 0)
