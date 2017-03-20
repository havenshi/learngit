# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop()
            result.insert(0,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result