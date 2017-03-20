# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return
        slow = head
        fast = head
        slow = slow.next
        fast = fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                # Lslow=K+M；Lfast=K+M+n*L；Lfast=2*Lslow。
                # 得出 Lslow=n*L；K=n*L-M。
                # slow重新回到head，而fast还在相遇点，slow和fast都向前走，且每次走一个节点。
                # 则slow从head走到起点走了K，而fast从相遇点出发也走了K，由于K=（n-1）*L+（L-M），所以fast转了n-1圈，再走L-M，也到了起点。
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return