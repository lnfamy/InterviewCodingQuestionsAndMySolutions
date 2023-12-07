"""
https://leetcode.com/problems/minimum-absolute-difference/
"""


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        # one traversal + counting sort!
        min_elem = min(arr)
        max_elem = max(arr)
        aux_arr = [0] * (max_elem - min_elem + 1)
        shift = -min_elem

        for elem in arr:
            aux_arr[elem + shift] = 1

        pairs = []
        min_diff = max_elem - min_elem
        prev = 0

        for curr in range(1, max_elem + shift + 1):
            # corresponding value doesn't exist in arr, so skip it
            if aux_arr[curr] == 0:
                continue

            # if its equal to the min_diff, we add it to the List
            if curr - prev == min_diff:
                pairs.append([prev - shift, curr - shift])
            # if it's smaller, we need to remake the pairs list
            elif curr - prev < min_diff:
                del pairs[:]
                min_diff = curr - prev
                pairs.append([prev - shift, curr - shift])
            prev = curr
        return pairs
