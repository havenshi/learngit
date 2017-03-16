class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        current = prices[0]
        prices_len = len(prices)
        profit = 0
        for i in range(1, prices_len):
            if prices[i] > current:
                profit += (prices[i] - current)
            current = prices[i]
        return profit