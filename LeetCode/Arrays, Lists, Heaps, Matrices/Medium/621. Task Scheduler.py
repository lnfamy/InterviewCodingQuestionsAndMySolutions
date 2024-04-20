"""
https://leetcode.com/problems/task-scheduler/
"""

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for i in range(len(tasks)):
            freq[ord(tasks[i]) - ord('A')] += 1
        freq.sort()
        # we substract 1 from freq[25] because we want the number of intervals, not occurences
        max_freq = freq[25] - 1
        # idle slots initialized to max freq element * cooldown period intervals (n)
        idle_slots = max_freq * n

        # now we iterate backwards from the second highest element frequency, to 'fill in' idle times if possible
        # to do so, at each step, we substract the minimum of the two: 1. max_freq, 2. current frequency
        # from idle slots
        for i in range(24, -1, -1):
            idle_slots -= min(max_freq, freq[i])

        # now after we've done that, we return the sum of the remaining idle slots (can be 0) to the number of tasks
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
