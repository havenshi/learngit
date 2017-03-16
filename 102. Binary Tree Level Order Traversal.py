import Queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = Queue.Queue()
        queue.put(root)  # record each layer
        allnode = []    # record val of item of each layer
        while not queue.empty():
            newlist = []
            count = 0 # count number for pop
            length = queue.qsize() # origin length
            while count < length:
                item = queue.get()
                newlist.append(item.val) # all val of item of each layer
                if item.left:                # add left
                    queue.put(item.left)
                if item.right:                # add right
                    queue.put(item.right)
                count += 1
            allnode.append(newlist)

            # now queue is empty
        return allnode
