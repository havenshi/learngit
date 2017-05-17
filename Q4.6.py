# binary search tree
def common(root, p, q):
    if not root:
        return None
    if p <= root.val and q > root.val:
        return root
    if p <= root.val and q <= root.val:
        return common(root.left, p, q)
    if p > root.val and q > root.val:
        return common(root.right, p, q)

# binary tree
def common2(root, p, q):
    if not root:
        return None
    if p == root.val or q == root.val:
        return root
    left = common2(root.left, p, q)
    right = common2(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right