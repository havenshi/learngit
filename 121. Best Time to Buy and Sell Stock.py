class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        result = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - low > result:
                result = prices[i] - low
            if prices[i] < low:
                low = prices[i]
        return result