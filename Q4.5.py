class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.result = []
        self.end = None

    def find(self, root, x):
        if not root:
            return None
        self.path(root, x, tmp = [])
        if self.result:
            if self.end.right:  # if has right node, next node should be right node's most left child node
                self.end = self.end.right
                while self.end.left:
                    self.end = self.end.left
                return self.end.val
            else:   # else, find parent which is greater than it
                for item in self.result[::-1]:
                    if item > x:
                        return item

    def path(self, root, x, tmp):
        tmp.append(root.val)
        if root.val == x:
            self.result = tmp
            self.end = root
        else:
            if root.left:
                copytmp = tmp[:]
                self.path(root.left, x, copytmp)
            if root.right:
                copytmp = tmp[:]
                self.path(root.right, x, copytmp)

if __name__ == '__main__':
    root = Tree(9)
    root.left = Tree(5)
    root.right = Tree(12)
    tmp = root.left
    tmp.left = Tree(4)
    tmp.right = Tree(7)
    tmp = tmp.right
    tmp.left = Tree(6)
    tmp.right = Tree(8)
    answer = Solution()
    print answer.find(root, 8)
