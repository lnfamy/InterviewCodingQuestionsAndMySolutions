"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid) - 1
        cols = len(grid[0]) - 1

        # to make the code cleaner, organize all possible steps to take
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def make_graph(row, col):
            for row_diff, col_diff in directions:
                new_r = row + row_diff
                new_c = col + col_diff

                # if the new indexes are illegal
                if not (0 <= new_r <= rows and 0 <= new_c <= cols):
                    continue

                # if the new indexes are non-traversable
                if grid[new_r][new_c] != 0:
                    continue

                yield (new_r, new_c)

        # first check before anything that it is possible to make a clean path at all:
        # if the top left cell and the bottom right cell are both 0
        if grid[0][0] != 0 or grid[rows][cols] != 0:
            return -1

        # now we set up the breadth first search
        q = collections.deque()
        # append our starting spot
        q.append((0, 0))
        # and start counting the length of the path we're taking
        grid[0][0] = 1

        while q:
            row, col = q.popleft()
            dist = grid[row][col]
            # exit condition: if we reached the bottom right cell i.e we found a clean path
            if (row, col) == (rows, cols):
                return dist

            for neighbor_row, neighbor_col in make_graph(row, col):
                grid[neighbor_row][neighbor_col] = dist + 1
                q.append((neighbor_row, neighbor_col))
        # if we reached here, that means the queue emptied before we found a clean path.
        # that means that there is no clean path.
        return -1
