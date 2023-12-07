"""
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
"""


# approach: DFS
class Solution:
    def averageOfSubtree(self, root) -> int:
        res = 0

        def postOrder(root):
            """
            to resolve the reference in the inner function to the variable
            res, which is declared 'out of scope', we declare the nonlocal
            variable.
            """
            nonlocal res
            # exit condition. if current node doesn't exist, we add nothing
            # to the sum or the count.
            if root is None:
                return 0, 0

            # recurse in postorder and save the results in variables
            left, l_count = postOrder(root.left)
            right, r_count = postOrder(root.right)

            """
            current_sum: this node's value + the left subtree's sum of values 
            + the right subtree's sum of values.
            current_count: the count of nodes in left and right subtrees plus 
            one for this current node.
            """
            current_sum = root.val + left + right
            current_count = 1 + l_count + r_count

            # if we found a node whose value is equal to its subtree's average,
            # we increment the res variable by 1
            if current_sum // current_count == root.val:
                res += 1

            return current_sum, current_count

        postOrder(root)
        return res
