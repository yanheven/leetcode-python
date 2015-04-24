__author__ = 'hyphen'
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        d={}
        max=0
        index=0
        for i in num:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
            if d[i]>max:
                max=d[i]
                index=i
        return index