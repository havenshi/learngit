# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: # 0 or 1 item
            return False
        slow = head
        fast = head
        # >2 item, omit the first time that slow == fast
        slow = slow.next
        fast = fast.next.next
        while fast and fast.next:  # do not judge slow, since fast ahead of slow is true
            slow = slow.next   # slow cursor move one step
            fast = fast.next.next # fast cursor move two steps
            if fast == slow:
                return True    # fast cross circle twice and reaches the slow
        return False   # fast reaches the end