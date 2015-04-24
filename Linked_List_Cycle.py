__author__ = 'hyphen'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        l=[]
        pre=None
        k={}
        while head:
            addr=id(head)
            if not pre:
                pre=addr
            elif k.get(addr):
                return True
            k[addr]=True
            head=head.next
        return False