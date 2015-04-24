__author__ = 'hyphen'
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        a=sorted(num)
        l=len(a)
        for i in range(l):
            b=target-a[i]
            for j in range(i+1,l):
                if a[j]==b:
                    x=num.index(a[i])+1
                    y=num.index(a[j])+1
                    if x==y:
                        y=num.index(a[j],x)+1
                    return (min(x,y),max(x,y))
                if a[j]>b:
                    break