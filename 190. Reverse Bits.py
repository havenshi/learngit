# -*- coding:utf8 -*-
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        new = 0
        for i in range(32):
            new = (new << 1) | ((n >> i) % 2)
            # n右移并%2得到二进制表达下的每位值。然后，new左移得到xxx0，'|' n的每位值，即xxx0可能变成xxx1。
        return new

if __name__ == "__main__":
    print Solution().reverseBits(43261596)