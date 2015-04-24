__author__ = 'hyphen'
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        days=len(prices)
        if days<2:
            return 0
        price=prices[0]
        profit=0
        empty=True
        if days==2:
            return max(prices[1]-prices[0],0)
        for i in range(days-1):
            if empty:
                if prices[i]<prices[i+1]:
                    price=prices[i]
                    empty=not empty
            else:
                if prices[i]>prices[i+1]:
                    empty=not empty
                    profit+=prices[i]-price
        if not empty:
            return profit+prices[days-1]-price
        return profit