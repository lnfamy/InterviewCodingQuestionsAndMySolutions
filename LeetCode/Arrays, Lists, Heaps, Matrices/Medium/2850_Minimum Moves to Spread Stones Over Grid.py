"""
https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/description/
"""


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # this list will hold the coordinates of the grid spaces that have no stones
        no_stones = []
        """
        this list will hold the coordinates of every single extra stone in the grid.
        example: say we have 3 stones at 2,2 - that means we'll have (2,2), (2,2) in the extra_stones list
        """
        extra_stones = []

        n = len(grid)

        for i, j in product(range(n), range(n)):
            stone = grid[i][j]

            if stone == 0:
                no_stones.append((i, j))
            # create new list, all of its elements is the tuple (i, j), repeated once for every extra
            # stone above 1.
            elif stone > 1:
                extra_stones.extend([(i, j)] * (stone - 1))

        # lambda function to calculate manhattan distance between any two points on the grid
        distance = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])

        """
        now we use permutations to generate all possible arrangements of the extra stones.
        for each arrangement, we calculate the sum of distances between the zeros and the current extra stones
        permutation, and then out of all that we choose the min sum of distances among all calculated
        permutations.
        """
        return min((sum(map(distance, no_stones, per))) for per in
                   set(permutations(extra_stones)))
