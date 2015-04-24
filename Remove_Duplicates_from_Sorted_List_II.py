__author__ = 'hyphen'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        j=ListNode(0)
        j.next=head
        pre=j
        cur=head
        while cur:
            while cur.next and pre.next.val==cur.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=cur
            else:
                pre.next=cur.next
            cur=cur.next
        return j.next