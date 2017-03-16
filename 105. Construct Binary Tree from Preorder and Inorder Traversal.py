# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # inorder:DBHEIAFCG
        # preorder:ABDEHICFG
        if not inorder:  # inorder base is [], not [] return True, [] == None return False.
            return None
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])  # find the middle position, left part and right part
        root.left = self.buildTree(preorder[1:1+pos], inorder[:pos])  # numbers of inorder and preorder are same
        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        return root