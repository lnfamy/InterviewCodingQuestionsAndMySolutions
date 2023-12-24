"""
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/
"""
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        operations = 0
        half = sum(nums) / 2
        # the default python function of heapify creates a minheap, therefore
        # to create a maxheap we do the 'reverse' - create a minheap of all
        # the negatives of the numbers
        heap = [-num for num in nums]
        heapq.heapify(heap)

        # this while loop will go on until we've reduced the array's sum at
        # least by half
        while half > 0:
            # extract number from the heap with a negative to get the real value
            n = -heapq.heappop(heap)
            # float division
            n /= 2.0
            half -= n
            # return the halved number into the heap
            heapq.heappush(heap, -n)
            operations += 1

        return operations
