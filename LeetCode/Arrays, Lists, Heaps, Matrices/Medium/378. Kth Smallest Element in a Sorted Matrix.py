"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""
from heapq import heappush, heappop
from typing import List

"""
approach: binary search
"""

class Solution:
    def binary_search(self, matrix, mid, smaller, larger):
        count = 0
        n = len(matrix)
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                # save the smallest number bigger than mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                # this element is less than or equal to the mid, so we'll save
                # the biggest number less than or equal to mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1
        return count, smaller, larger

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.binary_search(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger
            else:
                end = smaller

        return start

"""
approach: minheap
"""


class Solution_2:
    """
    min heap approach
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heap = []
        for r in range(min(k, m)):
            heappush(heap, (matrix[r][0], r, 0))

        ans = -1
        for i in range(k):
            ans, r, c = heappop(heap)
            if (c + 1) < n:
                heappush(heap, (matrix[r][c + 1], r, c + 1))
        return ans