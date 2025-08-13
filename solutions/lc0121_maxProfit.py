from typing import List

#本人题解：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/3751664/tan-xin-suan-fa-jie-mai-mai-gu-piao-de-z-htd6/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        maxprofit = 0
        minprice= prices[0]
        for i in range(n):
            minprice=min(minprice, prices[i])
            maxprofit=max(maxprofit, prices[i]-minprice)
        return maxprofit



