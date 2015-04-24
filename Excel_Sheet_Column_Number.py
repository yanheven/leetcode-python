__author__ = 'hyphen'
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result=0
        x=1
        for i in range(len(s)-1,-1,-1):
            result+=x*(ord(s[i])-64)
            x*=26
        return result