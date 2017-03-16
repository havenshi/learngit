# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        result = []
        count = 0
        while queue:
            newq = []
            newr = []
            for item in queue:
                newr.append(item.val)
                if item.left:
                    newq.append(item.left)
                if item.right:
                    newq.append(item.right)
            if count % 2 == 0:
                result.append(newr)
            else:
                result.append(newr[::-1])
            queue = newq
            count += 1
        return result

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
    print s.zigzagLevelOrder(head)