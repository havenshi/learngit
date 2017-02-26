# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        current = head
        previous = None
        while current != None:
            if previous != None and current.val == previous.val:
                previous.next = current.next  # remove current
                current = previous.next
            else:
                previous = current
                current = current.next
        return head