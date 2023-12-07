"""
https://leetcode.com/problems/detonate-the-maximum-bombs/description/
"""
import collections


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def b1_detonate_b2(b1: List[int], b2: List[int]) -> bool:
            return b1[2] ** 2 >= (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2

        # making a directed graph. for every bomb i, graph[i] will have a list of the bombs
        # that detonating bomb i will detonate as well
        graph = collections.defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if b1_detonate_b2(bombs[i], bombs[j]):
                    graph[i].append(j)

        # approach 3: bfs
        def bfs(i):
            queue = collections.deque([i])
            visited = set([i])
            while queue:
                current = queue.popleft()
                for neighbour in graph[current]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            return len(visited)

        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        return ans
