__author__ = 'hyphen'
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result=0
        for i in A:
            result=i^result
        return result