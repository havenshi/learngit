# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        result = []
        self.dfs(root, result, tmp=0)
        return sum(result)

    def dfs(self, node, result, tmp):
        tmp = tmp * 10 + node.val
        if not node.left and not node.right:
            result.append(tmp)

        if node.left:
            self.dfs(node.left, result, tmp)

        if node.right:
            self.dfs(node.right, result, tmp)
