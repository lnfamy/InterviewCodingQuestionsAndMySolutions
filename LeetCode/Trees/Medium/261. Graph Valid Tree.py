"""
https://leetcode.com/problems/graph-valid-tree/description/
"""
from typing import List

"""
    approach: union find
    let's first define a valid tree. 
    for the given graph to make a valid tree, it must have exactly n-1 edges (where n is the number of nodes).
    if it has less nodes, it cannot be fully connected, meaning the graph is not a single connected component.
    if it has any more, then it must contain cycles. 
    continuing off of this logic, if the graph is fully connected (one connected component) and it has exactly n-1
    edges, it can't possible contain a cycle - and must therefore be a valid tree.

    for the solution, we'll use union find. intuitive approach to problems with a "connected components" aspect 
    such as this one. we'll start it out where each element of the array is its own component, and then iterate
    over the edges and merge components as needed. in the end, we'll review the result of our traversal.
    """


class UnionFind:
    def __init__(self, n):
        # initialize n components for the n nodes of the graph
        self.parent = [node for node in range(n)]

    # method to find "representative" of the component that A is part of.
    # approach: go up the parent links until we reach the root node of A
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A

    # returns true if a merge happened, returns false otherwise
    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False
        self.parent[root_A] = root_B
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        unionf = UnionFind(n)

        # now for each edge we check if a merge happened - because if it didn't happen,
        # there must be a cycle in our graph - which makes it not a tree.
        for A, B in edges:
            if not unionf.union(A, B):
                return False

        return True