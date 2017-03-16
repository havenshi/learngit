class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bfs(self, root):
        queue = [root]
        result = []
        while queue:
            newq = []
            for item in queue:
                result.append(item.val)
                if item.left:
                    newq.append(item.left)
                if item.right:
                    newq.append(item.right)
            queue = newq
        return result

    def dfs_preorder1(self, root):  # while
        queue = [root]
        result = []
        while queue:
            node = queue.pop()
            result.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return result

    def dfs_preorder2(self, root):  # recursion
        result = []
        result.append(root.val)
        if root.left:
            result += self.dfs_preorder2(root.left)
        if root.right:
            result += self.dfs_preorder2(root.right)
        return result

    def dfs_inorder1(self, root):  # while
        queue = []
        result = []
        while root or queue:
            if root:
                queue.append(root)
                root = root.left
            else:
                root = queue.pop()
                result.append(root.val)
                root = root.right
        return result

    def dfs_inorder2(self, root):  # recursion
        result = []
        result.append(root.val)
        if root.left:
            result = self.dfs_inorder2(root.left) + result
        if root.right:
            result = result + self.dfs_inorder2(root.right)
        return result

    def dfs_postorder1(self, root):  # while
        queue = [root]
        result = []
        while queue:
            cur = queue.pop()
            result.insert(0, cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result

    def dfs_postorder2(self, root):  # recursion
        result = []
        if root.left:
            result = result + self.dfs_postorder2(root.left)
        if root.left:
            result = result + self.dfs_postorder2(root.right)
        result.append(root.val)
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
    print 'bfs is', s.bfs(head)
    print 'dfs_preorder is', s.dfs_preorder1(head)
    print 'dfs_preorder is', s.dfs_preorder2(head)
    print 'dfs_inorder is', s.dfs_inorder1(head)
    print 'dfs_inorder is', s.dfs_inorder2(head)
    print 'dfs_postorder is', s.dfs_postorder1(head)
    print 'dfs_postorder is', s.dfs_postorder2(head)