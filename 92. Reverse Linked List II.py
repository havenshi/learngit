# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        cons = ListNode(0)
        cons.next = head
        cur = cons.next
        pre = cons
        count = 0  # cursor to record the position
        while cur != None:
            count += 1
            if count == m:  # delete node m
                tmp1 = cur.val
                cur = cur.next
                pre.next = cur
                continue
            elif count == n:  # change the val of node n
                tmp2 = cur.val
                cur.val = tmp1
            pre = cur
            cur = cur.next

        cur = cons.next
        pre = cons
        count = 0
        while cur != None:
            count += 1
            if count == m:  # add new node
                newnode = ListNode(tmp2)
                pre.next = newnode
                newnode.next = cur
                break
            pre = cur
            cur = cur.next
        return cons.next