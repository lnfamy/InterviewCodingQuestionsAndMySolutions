"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

1.Given N boxes containing different number of Books in each box(numBook[i]),take a minimum number of books from the boxes conditions are such that:

you must take either all or none of the books inside a given box.
you cannot skip taking books from boxes adjacent to each other.Box1 and 2 can not be skipped but you can skip box 1 and 3.
you must have a minimum number of books in your hand
for example ,if there are 6 boxes and the number of books in box are {7,2,13,12,9,1} then the minimum number of books u can take is 15(by skipping box 1,3,5).

0>N>100

numBook[i]<10000

apparently the above question is very similar to the leetcode problem linked
"""
from typing import List


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         down_one = down_two = 0
#         for i in range(2, len(cost) + 1):
#             temp = down_one
#             down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
#             down_two = temp
#
#         return down_one

class solution2:
    def min_books(nums):
        length = len(nums)

        sum_array = [0] * length
        sum_array[0] = nums[0]
        sum_array[1] = nums[1]

        for i in range(2, length):
            sum_array[i] = nums[i] + min(sum_array[i - 1], sum_array[i - 2])

        return min(sum_array[length - 2], sum_array[length - 1])

    if __name__ == '__main__':
        # Example usage:
        nums = [7, 2, 13, 12, 9, 1]
        print(min_books(nums))  # Output should be 15

