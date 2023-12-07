"""
https://leetcode.com/problems/parallel-courses/description/
"""


class Solution:
    # general intuition: directed graph.
    # approach 3: combine from approach 2. in this solution we'll combine the helper functions find_cycle and longest_path
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # construct a directed graph from relations
        # {} = empty dictionary. i : [] = key-value pair in the dictionary.
        # for every i, there's a list [], initially empty. which we'll fill out later
        graph = {i: [] for i in range(1, n + 1)}
        for start_node, end_node in relations:
            graph[start_node].append(end_node)

        # check if graph contains a cycle
        visited = {}

        def dfs(node: int) -> int:
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1

            max_len = 1
            for end_node in graph[node]:
                length = dfs(end_node)
                if length == -1:
                    return -1
                else:
                    max_len = max(max_len, length + 1)
            visited[node] = max_len
            return max_len

        max_len = -1
        for node in graph.keys():
            length = dfs(node)
            if length == -1:
                return -1
            else:
                max_len = max(max_len, length)
        return max_len
