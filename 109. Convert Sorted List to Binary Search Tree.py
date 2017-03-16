# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = 0
        cur = head
        while cur:  # calculate the lenght of linked list
            length += 1
            cur = cur.next

        if length == 0:
            return None
        if length == 1:
            return TreeNode(head.val)
        if length == 2:
            root = TreeNode(head.next)
            root.left = TreeNode(head)

        left = head  # split left and right
        count = 0
        pre = None
        while head and count < length / 2:
            count += 1
            pre = head
            head = head.next
        # now head is on the position of length/2
        right = head.next  # right is after head
        pre.next = None  # pre is before head, set its next as None, then will get left

        root = TreeNode(head.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root