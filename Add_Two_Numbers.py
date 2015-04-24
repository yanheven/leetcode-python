__author__ = 'hyphen'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        carry=0
        q=None
        head=None
        while l1 and l2:
            digit=l1.val+l2.val+carry
            p=ListNode(digit%10)
            carry=digit/10
            l1=l1.next
            l2=l2.next
            if not head:
                head=p
                q=p
            else:
                q.next=p
                q=p
        while l1:
            digit=l1.val+carry
            p=ListNode(digit%10)
            carry=digit/10
            l1=l1.next
            q.next=p
            q=p
        while l2:
            digit=l2.val+carry
            p=ListNode(digit%10)
            carry=digit/10
            l2=l2.next
            q.next=p
            q=p
        if carry:
            p=ListNode(carry)
            q.next=p
        return head