# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:  # split list into part1 and part2. 1-2,3-4;1-3,4-5.
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None
        part1 = head

        revpart2 = ListNode(0)  # reverse part2
        while part2:
            tmp = ListNode(part2.val)
            tmp.next = revpart2.next
            revpart2.next = tmp
            part2 = part2.next
        revpart2 = revpart2.next

        while revpart2 and part1:  # merge part1 and revpart2
            tmp = ListNode(revpart2.val)
            tmp.next = part1.next
            part1.next = tmp
            part1 = part1.next.next
            revpart2 = revpart2.next