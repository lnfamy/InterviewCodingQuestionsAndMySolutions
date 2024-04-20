"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # base case - if linked list is empty, return null
        if not head:
            return None

        stack = []
        head_p = head

        # while there's items in our linked list
        while head:
            if head.child:
                # so as to not lose the nodes beyond this one when we traverse its children
                if head.next:
                    stack.append(head.next)
                # set the next node to be checked - the head's child
                head.next = head.child
                # set the child's prev node to be head, to 'flatten' their connection
                head.next.prev = head
                # to finish flattening their connection, set the parent's child pointer to None
                head.child = None
            # managing the nodes that we don't want to miss by checking the stack
            if not head.next and stack:
                node = stack.pop()
                if node:
                    head.next = node
                    node.prev = head
            head = head.next

        return head_p
