"""
https://leetcode.com/problems/merge-intervals/
"""
import collections


class Solution(object):
    # approach: brute force

    # this method checks overlap between intervals
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # make graph where there's an undirected edge between u and v iff u and v overlap
    def make_graph(self, intervals):
        graph = collections.defaultdict(list)

        for index, interval_index in enumerate(intervals):
            for j in range(index + 1, len(intervals)):
                if self.overlap(interval_index, intervals[j]):
                    graph[tuple(interval_index)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_index)

        return graph

    # merge all connected nodes in the given connected component and returns one interval
    def merge_nodes(self, nodes):
        # find the minimum first element of each interval in nodes
        minim = min(node[0] for node in nodes)
        maxim = max(node[1] for node in nodes)
        return [minim, maxim]

    # gets the connected components of the graph of the interval overlaps
    def get_components(self, graph, intervals):
        visited = set()
        component_count = 0
        node_in_comp = collections.defaultdict(list)

        def mark_comp(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    node_in_comp[component_count].append(node)
                    stack.extend(graph[node])

        # mark every node in the same connected component with the same integer
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_comp(interval)
                component_count += 1

        return node_in_comp, component_count

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = self.make_graph(intervals)
        node_in_comp, component_count = self.get_components(graph, intervals)

        # now, all intervals in every connected component will get merged
        return [self.merge_nodes(node_in_comp[comp]) for comp in
                range(component_count)]
