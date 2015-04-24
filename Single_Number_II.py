__author__ = 'hyphen'
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        once=0
        twice=0
        triple=0
        for i in A:
            triple=twice&i
            twice|=once&i
            once|=i
            once&=~triple
            twice&=~triple
        return once