__author__ = 'hyphen'
class Solution:
    # @return a string
    def intToRoman(self, num):
        s=''
        r=['I','IV','V','IX','X','XL',"L",'XC','C','CD','D','CM','M']
        a=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        for i in range(13):
            while num>=a[12-i]:
                s+=r[12-i]
                num-=a[12-i]
        return s