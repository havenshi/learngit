# -*- coding:utf8 -*-
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        size = len(prices)
        if 2 * k > size: # 操作所需元素超过了size，就可以无视k次的限制
            if len(prices) < 2:
                return 0
            current = prices[0]
            profit = 0
            for i in range(1, size):
                if prices[i] > current:
                    profit += (prices[i] - current)
                current = prices[i]
            return profit
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in range(size):
            for j in range(min(2 * k, i + 1) , 0 , -1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return dp

if __name__ == "__main__":
    print Solution().maxProfit(3, [2,4,2,4,2,4])