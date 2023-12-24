"""
https://leetcode.com/problems/count-fertile-pyramids-in-a-land/description/
"""


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        # each tip can only be used to pyramids of different heights starting from it down
        # we will modify the grid as we go to optimize the process, in a way that doesn't
        # interfere with finding other pyramids
        reverse_grid = []
        # backwards for loop, starts from len(grid) - 1, goes until -1, steps of -1
        for i in range(len(grid) - 1, -1, -1):
            reverse_grid.append(grid[i][:])
        output = self.pyramids(grid)
        output += self.pyramids(reverse_grid)
        return output

    def pyramids(self, grid):
        output = 0
        rows = len(grid)
        cols = len(grid[0])
        # tips can't be at the first/last row or column, therefore we don't check there
        for i in range(1, rows):
            for j in range(1, cols - 1):
                # if this cell is 1, and the cell directly above it is 1
                if grid[i][j] and grid[i - 1][j]:
                    grid[i][j] = min(grid[i - 1][j - 1], grid[i - 1][j + 1]) + 1
                    output += grid[i][j] - 1
        return output
