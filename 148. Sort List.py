# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        left = head
        slow.next = None  # use slow and fast cursor to split into 2 parts
        left = self.sortList(left)
        right = self.sortList(right)
        head = self.merge(left, right)
        return head

    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        # O(1) space, insert right into left
        if left.val <= right.val:
            result = left
            left = left.next
        else:
            result = right
            right = right.next
        tmp = result
        while left and right:
            if left.val <= right.val:
                tmp.next = left
                left = left.next
                tmp = tmp.next
            else:
                tmp.next = right
                right = right.next
                tmp = tmp.next
        if left == None:
            tmp.next = right
        if right == None:
            tmp.next = left
        return result