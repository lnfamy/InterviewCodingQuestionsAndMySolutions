"""
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
"""
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # sorting all event logs by timestamp, which is the first element of each log
        logs.sort(key=lambda x: x[0])

        # create union find data structure
        u = UnionFind(n)
        # initially, every person is a group of their own
        group_count = n

        for timestamp, fr_a, fr_b in logs:
            if u.union(fr_a, fr_b):
                group_count -= 1

            if group_count == 1:
                return timestamp

        return -1


class UnionFind:
    def __init__(self, size):
        self.group = [id for id in range(size)]
        # rank: heuristic that helps optimize the union() operation,
        # by helping create more balanced and less deep trees, which also improves
        # the efficacy of find() operations
        self.rank = [0] * size

    # this function finds the representative - the root of a group
    def find(self, person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, a, b):
        # replace nodes by roots/representatives
        rep_a = self.find(a)
        rep_b = self.find(b)

        merged = False
        if rep_a == rep_b:
            return merged

        merged = True
        # now merge the lower-rank group into the higher rank group
        if self.rank[rep_a] > self.rank[rep_b]:
            self.group[rep_b] = rep_a
        elif self.rank[rep_b] > self.rank[rep_a]:
            self.group[rep_a] = rep_b
        else:
            self.group[rep_a] = rep_b
            self.rank[rep_b] += 1
        return merged
