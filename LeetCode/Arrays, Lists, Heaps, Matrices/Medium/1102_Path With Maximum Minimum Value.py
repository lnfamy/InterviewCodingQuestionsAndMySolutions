"""
https://leetcode.com/problems/path-with-maximum-minimum-value/description/
"""


# approach 1: BFS. gives TLE
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        # this method checks whether a path with a score of val exists in the grid
        # ie. does a path where val is the min number is val exist in the grid
        def try_path(val):
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True

            # add the starting indices to the queue
            q = collections.deque([(0, 0)])
            while q:
                cur_row, cur_col = q.popleft()

                if cur_row == rows - 1 and cur_col == cols - 1:
                    return True

                # checking every possible move and if it's possible, adding it to the queue to be
                # visited.
                for dir_r, dir_c in directions:
                    new_row = cur_row + dir_r
                    new_col = cur_col + dir_c

                    # if the calculated new row and new col indices are illegal (out of borders)
                    # then skip over to the next iteration
                    if not (0 <= new_row <= rows - 1 and 0 <= new_col <= cols - 1):
                        continue

                    # checking if current cell has any unvisited neighbors with value >= val
                    if grid[new_row][new_col] >= val and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        q.append((new_row, new_col))

            # if we got here, that means the queue emptied before we ever made it to the bottom right
            # cell, meaning there's no path in the grid with min value val
            return False

        # set the initial 'score' that we're gonna check to be the minimum between
        # the top left cell and the bottom right cell, as those two cells are always guaranteed to be
        # in whatever path we make and therefore this saves unnecessary checks/iterations
        sc = min(grid[0][0], grid[rows - 1][cols - 1])
        while sc >= 0:
            if try_path(sc):
                return sc
            sc -= 1


# approach 2: union find
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # implement union find:
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1

        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # initializing the rank of all the cells. rank is to signify the depth of each group
        # in union find, therefore when we start and every cell is a group of its own, every rank
        # is 1 for every cell in the grid
        rank = [1] * (rows * cols)

        # initializing the list of roots for all cells. 'root', 'parent', 'representative' -
        # all different names for the same thing - an element in the group chosen to represent it
        # and all other elements in the group are associated with it. serves as an identifier for the group
        root = list(range(rows * cols))

        visited = [[False] * cols for _ in range(rows)]

        values = [(row, col) for row in range(rows) for col in range(cols)]
        # sort all cells by values. originally sorts from smallest to largest, so reverse = True makes
        # it sort from largest to smallest
        values.sort(key=lambda x: grid[x[0]][x[1]], reverse=True)

        # now we iterate over the sorted cells:
        for row, col in values:
            curr_pos = row * cols + col

            # mark current cell as visited
            visited[row][col] = True
            for dir_r, dir_c in directions:
                new_r = row + dir_r
                new_c = col + dir_c
                new_pos = new_r * cols + new_c

                # check if this cell has any visited neighbors with an equal or bigger value
                if 0 <= new_r < rows and 0 <= new_c < cols and visited[new_r][new_c]:
                    # if it does, we can connect their groups using the union method
                    union(curr_pos, new_pos)

            # if the top left cell is connected to the bottom right cell, that means we found a path
            # from start to finish
            if find(0) == find(rows * cols - 1):
                # and in that case, we return the value of the current cells
                # this cell is necessarily the biggest possible minimum of a path connecting
                # top left and bottom right because we sorted the values in descending order
                # and went through the grid by values
                return grid[row][col]
        return -1
