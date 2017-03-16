# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        result = []
        queue = [root]
        while queue:
            node = queue.pop()
            result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        pre = root
        i = 1
        while i < len(result):
            root.left = None
            root.right = TreeNode(result[i])
            root = root.right
            i += 1
        root = pre

