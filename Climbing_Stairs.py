__author__ = 'hyphen'
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        m=n+2
        s=[0]*(m)
        s[1]=1
        s[2]=2
        for i in range(3,m):
            s[i]=s[i-2]+s[i-1]
        return s[n]