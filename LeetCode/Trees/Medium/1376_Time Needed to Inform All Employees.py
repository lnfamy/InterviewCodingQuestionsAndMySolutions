"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
"""


class Solution:
    # approach: DFS top-down
    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        adj_list = [[] for i in range(n)]

        # making adjacency list of all 'brothers' - employees who are direct
        # subordinates of the same manager, for every manager
        for i, m in enumerate(manager):
            if m > -1:
                adj_list[m].append(i)

        def dfs(i):
            """
            here, for each manager of index i, we iterate through all their subordinates
            as seen by the for loop inside the brackets using the iterator j. so for each subordinate
            j of manager i, we calculate the inform time using this recursive dfs function, and out of those
            subordinate times calculated we return the biggest one. + informTime[i] takes care of the
            inform time of the current employee to its own subordinates
            """
            return max([dfs(j) for j in adj_list[i]] or [0]) + informTime[i]

        return dfs(headID)
