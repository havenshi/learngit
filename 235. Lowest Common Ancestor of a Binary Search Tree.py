# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if p.val >= q.val:
            p, q = q, p # make sure p is smaller
        if p.val <= root.val and q.val >= root.val:
            # if root value is in the middle of p and q, return root.
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) # common root must be on left
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) # common root must be on right