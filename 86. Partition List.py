# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(0)
        small2 = small
        large = ListNode(0)
        large2 = large
        while head != None:  # create small and large
            small2.next = ListNode(head.val)
            small2 = small2.next
            large2.next = ListNode(head.val)
            large2 = large2.next
            head = head.next

        current = small.next
        previous = small
        while current != None:
            if current.val >= x:  # delete val greater than or equal to x
                previous.next = current.next
                current = previous.next
            else:  # move on
                previous = current
                current = current.next

        current2 = large.next
        previous2 = large
        while current2 != None:
            if current2.val < x:  # delete val smaller than x
                previous2.next = current2.next
                current2 = previous2.next
            else:  # move on
                previous2 = current2
                current2 = current2.next

        # concatenate small and large
        previous.next = large.next
        return small.next


if __name__ == "__main__":
    lst = ListNode(1)
    lst.next = ListNode(2)
    s = Solution()
    x = s.partition(lst, 2)
    while x != None:
        print x.val
        x = x.next