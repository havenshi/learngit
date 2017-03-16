# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        result = []
        while queue:
            newq = []
            newr = []
            for item in queue:
                newr.append(item.val)
                if item.left:
                    newq.append(item.left)
                if item.right:
                    newq.append(item.right)
            queue = newq
            result.append(newr)
        return result[::-1]