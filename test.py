# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                if root.next:
                    if root.next.left:
                        root.right.next = root.next.left
                    if root.next.right:
                        root.right.next = root.next.right
                else:
                    root.right.next = None
            if root.left:
                if root.next:
                    if root.next.left:
                        root.left.next = root.next.left
                    if root.next.right:
                        root.left.next = root.next.right
                else:
                    root.left.next = None
            if root.right:
                if root.next:
                    if root.next.left:
                        root.right.next = root.next.left
                    if root.next.right:
                        root.right.next = root.next.right
                else:
                    root.right.next = None
            self.connect(root.left)
            self.connect(root.right)