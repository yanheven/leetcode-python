__author__ = 'hyphen'
class Solution:
    # @return an integer
    def numTrees(self, n):
        l=[0]*(n+2)
        l[0]=1
        l[1]=1
        l[2]=2
        for i in range(3,n+1):
            for j in range(1,n+1):
                l[i]+=(l[i-j]*l[j-1])
        return l[n]