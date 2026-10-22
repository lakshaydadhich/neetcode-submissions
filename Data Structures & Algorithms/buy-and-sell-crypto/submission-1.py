class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        min=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min:
                min=prices[i]
            profit=prices[i]-min

            if profit>max:
                max=profit
        return max