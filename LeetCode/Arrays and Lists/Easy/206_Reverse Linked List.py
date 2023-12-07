"""
https://leetcode.com/problems/reverse-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    #iterative solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #while we go through the linked list, we'll change every node's next pointer to point at the previous node
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        #by the time we've finished iterating over the list, current is none and prev is now the new head
        return prev
    """

    # recursive solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
