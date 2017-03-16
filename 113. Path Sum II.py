# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        self.dfs(root, result, tmp=[], target=sum)
        return result

    def dfs(self, node, result, tmp, target):
        tmp.append(node.val)
        if not node.left and not node.right:
            if sum(tmp) == target:
                result.append(tmp)

        if node.left:
            copytmp = tmp[:]
            self.dfs(node.left, result, copytmp, target)

        if node.right:
            copytmp = tmp[:]
            self.dfs(node.right, result, copytmp, target)