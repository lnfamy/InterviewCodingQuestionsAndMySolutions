"""
https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
"""


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        r = [0] * rows
        c = [0] * cols

        # handling duplicates: 1. sort the values in the matrix in non-increasing order.
        #                     2. for each value v, store all the instance positions of v (x,y) in a
        #                     3. reverse indexed list
        val_map = {}
        from sortedcontainers import SortedSet
        s = SortedSet()
        for i in range(0, rows):
            for j in range(0, cols):
                # if the value isn't in the map, initialize an empty list for it
                # save all instances in the list of every value in the given matrix
                if not -mat[i][j] in val_map:
                    val_map[-mat[i][j]] = []
                val_map[-mat[i][j]].append([i, j])
                s.add(-mat[i][j])
        # this is where we find the longest path for each value, from largest to smallest
        # for every occurence position x,y - we save the longest path (row or column, whichever is bigger) + 1
        # to account for the current cell. we store that in temp[x][y].
        # then, we check if r[x] (longest path on row x) needs an update. because if temp[x][y] holds c[y] and it's
        # bigger than r[x], that'll be the new value of it. same goes for c[y].
        temp = [[0] * cols for _ in range(rows)]
        for x in s:
            for val in val_map.get(x):
                temp[val[0]][val[1]] = max(r[val[0]], c[val[1]]) + 1
            for val in val_map.get(x):
                r[val[0]] = max(r[val[0]], temp[val[0]][val[1]])
                c[val[1]] = max(c[val[1]], temp[val[0]][val[1]])
        # now, to find the ultimate longest path, we take the bigger of the row and column longest-path arrays
        return max(max(r), max(c))
