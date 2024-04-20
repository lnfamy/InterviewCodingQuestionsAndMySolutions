"""
https://leetcode.com/problems/rotting-oranges/description/
"""
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        gRows = len(grid)
        gCols = len(grid[0])
        rotting = 0
        fresh = 0
        # step 1: build initial set of rotting oranges:
        for i in range(gRows):
            for j in range(gCols):
                if grid[i][j] == 2:
                    q.append((i, j))
                    rotting += 1
                elif grid[i][j] == 1:
                    fresh += 1

        # we append a "ticker" of our timestamp, i/e a dummy element to the end of the queue
        q.append((-1, -1))

        # step 2: start rotting the oranges minute by minute, using BFS
        mins = -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # while q == while there's rotting oranges in the queue - we only inserted rotting oranges into it
        while q:
            row, col = q.popleft()
            if row == -1:
                # one round of processing is over
                mins += 1
                if q:
                    q.append((-1, -1))
            else:
                for d in directions:
                    n_row = row + d[0]
                    n_col = col + d[1]
                    # quick check that we're within the grid bounds
                    if gRows > n_row >= 0 and gCols > n_col >= 0:
                        # if this orange is fresh, it'll be rotten
                        if grid[n_row][n_col] == 1:
                            grid[n_row][n_col] = 2
                            fresh -= 1
                            # this orange can now contaminate the others
                            q.append((n_row, n_col))
        return mins if fresh == 0 else -1
