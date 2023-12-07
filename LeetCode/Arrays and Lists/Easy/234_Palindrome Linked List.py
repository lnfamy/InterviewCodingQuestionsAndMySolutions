"""
https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # approach: compare against reversed second half of the list
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        mid = self.find_second_half(head)
        sec_half = self.reverse(mid.next)

        first_half_ptr = head
        sec_half_ptr = sec_half
        res = True
        while res and sec_half_ptr:
            if first_half_ptr.val != sec_half_ptr.val:
                res = False
            first_half_ptr = first_half_ptr.next
            sec_half_ptr = sec_half_ptr.next

        mid.next = self.reverse(sec_half)
        return res

    def find_second_half(self, head):
        fast = slow = head
        # when fast reaches the end, slow reaches the halfway point
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
