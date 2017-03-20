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
        head1 = head
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head

    def merge(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        result = ListNode(0)
        tmp = result
        while head1 and head2:
            if head1.val <= head2.val:
                tmp.next = head1
                head1 = head1.next
                tmp = tmp.next
            else:
                tmp.next = head2
                head2 = head2.next
                tmp = tmp.next
        if head1 == None:
            tmp.next = head2
        if head2 == None:
            tmp.next = head1
        return result.next