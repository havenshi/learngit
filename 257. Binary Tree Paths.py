# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        result = []
        self.dfs(root, result, tmp=[])
        return result

    def dfs(self, node, result, tmp):
        tmp.append(str(node.val))
        if not node.left and not node.right:
            result.append('->'.join(tmp))

        if node.left:
            copytmp = tmp[:]
            self.dfs(node.left, result, copytmp)

        if node.right:
            copytmp = tmp[:]
            self.dfs(node.right, result, copytmp)

if __name__ == "__main__":
    head = TreeNode(6)
    current = head
    current.right = TreeNode(10)
    current.left = TreeNode(4)
    current = current.left
    current.left = TreeNode(1)
    current.right = TreeNode(5)
    current = head
    current = current.right
    current.right = TreeNode(15)
    current.left = TreeNode(8)
    prev = current
    current = current.left
    current.left = TreeNode(7)
    current.right = TreeNode(9)
    current = prev
    current = current.right
    current.left = TreeNode(12)
    current.right = TreeNode(18)

    s = Solution()
    print s.binaryTreePaths(head)

