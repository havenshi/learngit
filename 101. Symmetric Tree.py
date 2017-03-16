# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.help(root.left, root.right)

    def help(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val:
            return self.help(p.right, q.left) and self.help(p.left, q.right)
        return False