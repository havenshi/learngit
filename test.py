def swaptree(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root.left == None and root.right == None:
        return root
    else:
        root.left.val, root.right.val = root.right.val, root.left.val
        self.swaptree(root.left)
        self.swaptree(root.right)