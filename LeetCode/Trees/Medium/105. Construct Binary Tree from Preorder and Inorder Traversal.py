"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    preorder[0] is always the tree's root
    and since preorder and inorder all consist of unique values, this means that the first
    appearance of preorder[0] in inorder, will be what divides our inorder array like so:

    left subtree -- preorder[0] -- right subtree

    and then preorder[1] would be the root of a subtree -and when we find it in the inorder traversal, it'll
    follow the same aforementioned structure of left subtree -- preorder[1] -- right subtree
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # make hashmap to store indices of elements in inorder list
        inorder_map = {val: i for i, val in enumerate(inorder)}

        # making recursive function to build the tree (divide and conquer approach based on the
        # earlier explanation of the solution approach)
        def build(p_start, p_end, in_start, in_end):
            # exit condition: if start index preorder list is greater than its end index,
            # that means that the current subtree is null - return None
            if p_start > p_end:
                return None

            # get value of root node from preorder list using the start index, use that value to build the TreeNode
            root_value = preorder[p_start]
            root = TreeNode(root_value)

            # find index of root node's value in the inorder list using the hashmap
            inorder_i = inorder_map[root_value]

            # determine size of the left subtree
            left = inorder_i - in_start

            # now, recursively build the left subtree
            root.left = build(p_start + 1, p_start + left, in_start, inorder_i)
            # recursively build the right subtree
            root.right = build(p_start + left + 1, p_end, inorder_i + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
