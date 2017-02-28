# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]
        lst = []
        for i in range(start, end+1):
            left = self.dfs(start, i-1)
            right = self.dfs(i+1, end)
            for x in left:
                for y in right:
                    root = TreeNode(i)
                    root.left = x
                    root.right = y
                    lst.append(root)
        return lst