"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
"""
import collections


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # we want to make sure we're utilizing every single 'empty' seat in the cars
        # and that we minimize the number of cars used to minimize the amount of fuel used
        # therefore it makes sense that we want to go from the bottom up.
        # for each node, we want to move all representatives in its subtrees to itself to minimize cars
        # here we use DFS to compute the number of representatives in each subtree.

        # create graph. for each node we need to know its neighbours because they share a common parent
        adj = collections.defaultdict(list)
        # for each city, we make a list of neighbouring cities - ie. cities at the same tree level
        for x, y in roads:
            adj[x].append(y)
            adj[y].append(x)

        self.ans = 0

        # explicitly set people to 1 for convenience. we don't iterate with people because we're counting
        # the number of people in every subtree and not the tree as a whole
        def dfs(index, prev, people=1):
            for x in adj[index]:
                # if the neighbor x is the same as the previous city, skip (ensuring each city is only visited once)
                if x == prev:
                    continue
                # call this function for each neighbour x
                people += dfs(x, index)
            if index:
                # here you can see we put the answer in terms of how many people can fit in the available cars
                # we calculate for each subtree the number of people arriving to it divided by the number of seats
                # available in a car - and that's the minimum number of cars needed to reach the next parent.
                # the minimum number of cars needed to reach the next parent is of course the fuel needed,
                # as each traversal from city to city (node to node) costs 1 litre of fuel.
                self.ans += int(math.ceil(people / seats))
            return people

        # we start going through the tree, starting from the root node.
        # the way that this function works is that for each node, it'll calculate the number of people in
        # its subtrees. we prevent redundant calls and double counts, and on the way we calculate
        # the answer
        dfs(0, 0)
        return self.ans
