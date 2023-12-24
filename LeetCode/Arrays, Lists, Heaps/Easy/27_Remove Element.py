"""
https://leetcode.com/problems/remove-element/description/
"""


class Solution:
    # problem determines that it doesn't matter what remains in the array beyond the new length
    # therefore we don't actually have to remove the target elements, just displace them

    """
    first approach: remove the elements by 'rewriting' every element different from val into the first
    k elements of the array, where 1-k is the number of target elements.

    def removeElement_v1(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    """
    """
    second approach:
    we iterate over the array while keeping two int variables: i is the current index we use to traverse the array
    and length is the 'current' length of the array, which we 'modify' in logic but not in the computers memory
    when we find a target value, that is, a value in nums[] that equals val, we switch it out with the current last 
    element in the array, and then 'delete' it by decrementing the variable length, which we also use to traverse 
    the array.
    in the end, the variable length signifies how many non target values we have, which is the required thing to return.
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1
        return length
