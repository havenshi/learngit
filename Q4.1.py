class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isBalance(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    else:
        if abs(length(root.left) - length(root.right)) <= 1 and isBalance(root.left) and isBalance(root.right):
            return True
    return False

def length(root, n = 0):
    if not root:
        return n
    return max(length(root.left, n+1), length(root.right, n+1))

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
tmp = root.left
tmp.left = Tree(4)
tmp = tmp.left
tmp.left = Tree(5)
print isBalance(root)