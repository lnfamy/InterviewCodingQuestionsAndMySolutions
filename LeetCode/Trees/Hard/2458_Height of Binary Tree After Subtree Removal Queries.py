"""
https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
"""
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[
        int]:
        depth = collections.defaultdict(int)
        height = collections.defaultdict(int)

        def depth_height(node, d):
            if not node:
                return -1
            depth[node.val] = d
            left = depth_height(node.left, d + 1)
            right = depth_height(node.right, d + 1)
            h = max(left, right) + 1
            height[node.val] = h
            return h

        depth_height(root, 0)

        # cousins = same level nodes in other parts of the tree
        # here is where we find the cousins of each level
        cousins = collections.defaultdict(list)
        for val, d in depth.items():
            cousins[d].append((-height[val], val))
            cousins[d].sort()
            while len(cousins[d]) > 2:
                cousins[d].pop()

        # here is where we get the end result
        res_arr = []
        for val in queries:
            d = depth[val]
            csn = cousins[d]
            if len(csn) == 1:
                res_arr.append(d - 1)
            elif val == csn[0][
                1]:  # if the removed node has max height in cousins
                res_arr.append(d - csn[1][0])
            else:
                res_arr.append(d - csn[0][0])
        return res_arr