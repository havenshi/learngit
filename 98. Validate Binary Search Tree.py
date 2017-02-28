# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, min=float('-inf'), max=float('inf'))

    def dfs(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.dfs(root.left, min, root.val) and self.dfs(root.right, root.val, max)