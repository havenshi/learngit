# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # method 1 time limit exceeded
        res = ListNode(0)
        res.next = head
        tmp = res
        count = res

        head1 = head  # first head 1-5, walk through first
        head2 = res  # second head 0-5, walk through left node

        if head == None:
            return []
        if k == 0:
            return head

        num = 0
        while count.next != None:
            num += 1
            count = count.next
        if num <= k:
            return head

        i = 0
        while i < k and head1 != None and head1.next != None:
            head1 = head1.next  # head1 jump from 1 to 3
            i += 1

        while head1 != None:  # head1 has 3-5 three nodes left
            head1 = head1.next  # head1 3-5
            head2 = head2.next  # head2 0-3
            tmp = tmp.next  # create a list 0-3
        tmp.next = None  # set end, tmp 0-3

        tmp2 = head2  # tmp2 begin with 4, 4-5

        while head2.next != None:
            head2 = head2.next

        head2.next = res.next  # add 1-3
        return tmp2.next


        # method 2
        if head==None:
            return head
        curNode = head
        size = 0
        while curNode!=None:
            size += 1
            curNode = curNode.next
        k = k%size
        if k==0:         # return head
            return head
        len = 1
        curNode = head
        while len<size-k:
            len += 1
            curNode = curNode.next  # curNode forward 3
        newHead = curNode.next      # newHead forward 4
        curNode.next = None         # curNode foward null, head now 1-3
        curNode = newHead           # curNode forward 4
        while curNode.next!=None:
            curNode = curNode.next  # curNode traversal 4-5
        curNode.next = head         # curNode forward head
        return newHead

