# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        cur = head.next
        beforecur = head
        while cur:
            tmp = head
            beforetmp = None
            while cur and tmp.val < cur.val:  # find the before node which is greater than cur
                beforetmp = tmp
                tmp = tmp.next

            if tmp == cur:  # if no before node greater than cur, continue
                beforecur = tmp
                cur = cur.next
                continue

            tmpnode = ListNode(cur.val)  # 3(tmp)-2(beforecur)-4(cur)
            tmpnode.next = tmp
            beforecur.next = cur.next
            if beforetmp:
                beforetmp.next = tmpnode
            else:
                head = tmpnode

            cur = beforecur.next  # cur already removed, set cur as beforecur.next

        return head