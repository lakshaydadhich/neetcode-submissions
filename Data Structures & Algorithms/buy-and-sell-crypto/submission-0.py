class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        max=0
        for i in range(1,len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
    
            profit=prices[i]-minprice

            if profit>max:
                max=profit
        return max
       