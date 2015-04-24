__author__ = 'hyphen'
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        cnt=0
        i=0
        a=[0]*n
        while i>=0:
            a[i]+=1
            while a[i]<=n and not self.ok(a,i):
                a[i]+=1
            if a[i]<=n:
                if i==n-1:
                    cnt+=1
                else:
                    i+=1
                    a[i]=0
            else:
                i-=1
        return cnt

    def ok(self,a,i):
        for j in range(i):
            if a[i]==a[j] or abs(a[i]-a[j])==abs(i-j):
                return False
        return True