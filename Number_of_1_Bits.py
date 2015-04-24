__author__ = 'hyphen'
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        hw=0
        while n:
            hw+=n%2
            n=n>>1
        return hw