"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution(object):
    """
    this is going to be a brute force sort of approach as there won't be logical shortcuts,
    but it's still efficient using the two pointer array traversal approach.

    pointers arent native to python, therefore we'll use int variables named l and r
    """

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while (l < r):
            sum = numbers[r] + numbers[l]
            # if its greater than target, we want to decrease so we move the rightmost pointer
            # backwards, as the array is sorted in a non decreasing order
            if sum > target:
                r -= 1
            # exact opposite of prev comment
            elif sum < target:
                l += 1
            # this else means that numbers[r] + numbers[l] == target
            else:
                return [l + 1, r + 1]
        return
