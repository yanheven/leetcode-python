__author__ = 'hyphen'
class Solution:
    # @return an integer
    def romanToInt(self, s):
        l=len(s)
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=r[s[0]]
        for i in range(1,l):
            if r[s[i-1]]<r[s[i]]:
                n+=r[s[i]]-2*r[s[i-1]]
            else:
                n+=r[s[i]]
        return n