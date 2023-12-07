"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    splicing the heads from each list to merge them into a sorted list
    so if head2 >= head1 , head1 will be the head of the new list

    approaches:
    1. recursion:
        exit condition:
        either list is empty

        recursion body:
        splice both heads of the lists and put them into variables.
        compare heads by value. append to a list that's sent into the recursive function

    """
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #first: exit conditions
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        #recursion body
        elif list2.val >= list1.val:
            #recursive call, this is where the next item of the final returned list is defined
            #in this case the next item is from list1
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            #recursive call, other case 
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    """

    """
    iterative approach:
    1. while both lists are not empty, iterate over them and compare the heads 
    2. we insert them in non decreasing order into a new list basically, which will be returned at the end
    """

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # new head - used to keep track of the final list's head node.
        # itr head is used to keep track of the current node in the merged list
        # creating a new list
        new_head = itr_head = ListNode()
        while list1 and list2:
            # if list2's head is bigger, we want list1 to be first
            if list2.val >= list1.val:
                itr_head.next = list1
                list1 = list1.next
            else:
                itr_head.next = list2
                list2 = list2.next
            itr_head = itr_head.next

        if list1:
            itr_head.next = list1
        if list2:
            itr_head.next = list2

        return new_head.next
