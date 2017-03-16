# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root, layer=0)

    def depth(self, root, layer):
        if root == None:
            return layer
        layer += 1
        if not root.left and not root.right:  # it's a leaf, return layer directly
            return layer
        if root.left and root.right:  # has left and right, find min
            return min(self.depth(root.left, layer), self.depth(root.right, layer))
        if root.left:  # if left or right, it is not a leaf
            return self.depth(root.left, layer)
        if root.right:  # if left or right, it is not a leaf
            return self.depth(root.right, layer)