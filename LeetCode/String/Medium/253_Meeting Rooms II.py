"""
https://leetcode.com/problems/meeting-rooms-ii/description/
"""


class Solution:
    # approach: minheap
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 0
        nearest_ending = [0]
        for start, end in intervals:
            if rooms == 0:
                rooms += 1
                nearest_ending.pop()
            elif nearest_ending[0] > start or nearest_ending[0] == end:
                rooms += 1
            else:
                nearest_ending[0] = nearest_ending[-1]
                nearest_ending.pop()
            nearest_ending.append(end)
            heapq.heapify(nearest_ending)

        return rooms
