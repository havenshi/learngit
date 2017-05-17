class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # m = len(dungeon)
        # n = len(dungeon[0])
        # dungeon[m-1][n-1] = 1 - dungeon[m-1][n-1]
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i == m-1 and j == n-1:
        #             continue
        #         if i == m-1:
        #             dungeon[i][j] = dungeon[i][j+1] - dungeon[i][j]
        #             continue
        #         if j == n-1:
        #             dungeon[i][j] = dungeon[i+1][j] - dungeon[i][j]
        #             continue
        #         tmp1 = dungeon[i+1][j] - dungeon[i][j]
        #         tmp2 = dungeon[i][j+1] - dungeon[i][j]
        #         if tmp1 < 1:
        #             dungeon[i][j] = tmp2
        #         elif tmp2 < 1:
        #             dungeon[i][j] = tmp1
        #         else:
        #             dungeon[i][j] = min(tmp1, tmp2)
        # return dungeon

        w = len(dungeon[0])
        h = len(dungeon)
        hp = [[0] * w for x in range(h)]

        hp[h - 1][w - 1] = max(0, -dungeon[h - 1][w - 1]) + 1

        for x in range(h - 1, -1, -1):
            for y in range(w - 1, -1, -1):
                down = None
                if x + 1 < h:
                    down = max(1, hp[x + 1][y] - dungeon[x][y])
                right = None
                if y + 1 < w:
                    right = max(1, hp[x][y + 1] - dungeon[x][y])
                if down and right:
                    hp[x][y] = min(down, right)
                elif down:
                    hp[x][y] = down
                elif right:
                    hp[x][y] = right
        return hp[0][0]
if __name__ == "__main__":
    print Solution().calculateMinimumHP([[10,4,-48,-8,-87,9],[49,-100,6,-15,41,-99],[-76,-45,-26,50,46,14],[-81,-92,46,-62,-26,1],[-44,19,26,-98,-49,-72]])