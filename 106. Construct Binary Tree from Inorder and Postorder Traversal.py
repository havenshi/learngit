# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:pos], postorder[:pos])
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])
        return root