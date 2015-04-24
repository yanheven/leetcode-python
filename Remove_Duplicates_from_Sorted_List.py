__author__ = 'hyphen'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        i=j=head
        while i:
            while i.next and i.val==i.next.val:
                i.next=i.next.next
            i=i.next
        return j