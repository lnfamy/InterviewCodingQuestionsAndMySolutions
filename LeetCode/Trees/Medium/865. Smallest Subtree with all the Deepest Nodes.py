"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    approach: dfs
    go through the tree using dfs, until we reach the deepest level's node
    we then pass the level back to the parent and compare the parents' subtrees.
    if the subtrees are of the same depth, return said depth and the parent node
    otherwise, return the deeper subtree of the two and its depth.
    """

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root, level):
            if not root:
                return level, None

            left_lev, left_node = dfs(root.left, level + 1)
            right_lev, right_node = dfs(root.right, level + 1)

            if right_lev > left_lev:
                return right_lev, right_node
            if left_lev > right_lev:
                return left_lev, left_node
            return left_lev, root

        return dfs(root, 0)[1]
