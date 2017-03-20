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
                print profit
            current = prices[i]
        return profit

if __name__ == '__main__':
    answer = Solution()
    print answer.maxProfit([2,1,4,5])