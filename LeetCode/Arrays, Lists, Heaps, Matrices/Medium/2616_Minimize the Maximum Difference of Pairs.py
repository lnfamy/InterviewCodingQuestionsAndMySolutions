"""
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
"""


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        # using greedy approach to find p valid pairs
        def valid_pairs(threshold):
            index = 0
            count = 0
            while index < n - 1:
                # if a pair is found, we skip two indexes and update the count +1
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        # use binary search to find the threshold
        left = 0
        # right = max - min of the array to give us the max threshold for the search
        right = nums[-1] - nums[0]

        while left < right:
            mid = left + (right - left) // 2
            # if we found enough pairs in this one, we look for a smaller threshold
            # otherwise, we look for a larger threshold
            if valid_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left
