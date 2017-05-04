# Given a binary tree where all the right nodes are either leaf nodes with a sibling
# (a left node that shares the same parent node) or empty, flip it upside down and
# turn it into a tree where the original right nodes turned into left leaf nodes.
# Return the new root.
#
# For example:
# Given a binary tree {1,2,3,4,5},
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# return the root of the binary tree [4,5,2,#,#,3,1].
#
#    4
#   / \
#  5   2
#     / \
#    3   1
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        if not root:
            return None
        if not root.left:
            return root
        new = self.upsideDownBinaryTree(root.left)  # 1. set left to be a new root
        tmp = new
        while tmp.right:     # reach the most right leaf node
            tmp = tmp.right
        tmp.right = TreeNode(root.val)  # 2. right is origin root value
        if root.right:     # 3. left is origin right value of root
            tmp.left = TreeNode(root.right.val)
        return new

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    tmp = root.left
    tmp.right = TreeNode(5)
    tmp.left = TreeNode(4)
    answer = Solution()
    result = answer.upsideDownBinaryTree(root)
    print result.val, result.left.val, result.right.val, result.right.left.val, result.right.right.val