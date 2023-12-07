"""
https://leetcode.com/problems/delete-nodes-and-return-forest/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del_set = set(to_delete)
        result = []

        def recurse(root, is_root):
            # exit conditions:   1. If the given root is null, return null
            # is_root = True if this node's parent is gone. so basically, is_root == True if node is an orphan
            if not root:
                return None
            # root_deleted == True if this node's value is in the to_delete set.
            root_deleted = root.val in to_del_set
            if is_root and not root_deleted:
                result.append(root)
            root.left = recurse(root.left, root_deleted)
            root.right = recurse(root.right, root_deleted)
            if root_deleted:
                return None
            else:
                return root

        recurse(root, True)
        return result
