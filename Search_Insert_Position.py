__author__ = 'hyphen'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l=len(A)
        for i in range(l):
            if target==A[i]:
                return i
            if target<A[i]:
                    return i
        return l