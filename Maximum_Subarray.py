__author__ = 'hyphen'
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        sum=-1
        tmp=0
        for i in range(len(A)):
            tmp+=A[i]
            if tmp>0:
                sum=max(sum,tmp)
            else:
                tmp=0
        if sum<0:
            sum=A[0]
            for i in range(len(A)):
                sum=max(sum,A[i])
        return sum