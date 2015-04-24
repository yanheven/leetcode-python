__author__ = 'hyphen'
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        l=len(A)
        index=0
        newl=1
        dup=False
        if l<2:
            return l
        for i in range(1,l):
            if A[i]==A[index] and not dup:
                newl+=1
                index+=1
                A[index]=A[i]
                dup=not dup
            if A[i]!=A[index]:
                newl+=1
                index+=1
                A[index]=A[i]
                dup=False
        return newl