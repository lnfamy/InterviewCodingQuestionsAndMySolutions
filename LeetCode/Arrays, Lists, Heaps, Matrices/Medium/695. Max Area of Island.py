"""
https://leetcode.com/problems/max-area-of-island/description/
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (not 0 <= r < rows
                    or not 0 <= c < cols
                    or grid[r][c] == 0):
                return 0

            # mark current cell as 0 as in 'visited' so that we don't check it again
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        return max(dfs(r, c) for r in range(rows) for c in range(cols))
