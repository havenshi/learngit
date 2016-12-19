class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0);
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next # jump 2nd node

            tmp.next = p.next      # add 1st
            p.next = tmp

            p = p.next.next        # forward two steps
        return dummy.next