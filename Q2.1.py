class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def remove(self, head):
        if not head or not head.next:
            return head
        cur = head
        while cur:
            pre = cur
            tmp = cur.next
            while tmp:
                if tmp.val == cur.val:
                    pre.next = pre.next.next
                    tmp = pre.next
                else:
                    pre = tmp
                    tmp = tmp.next
            cur = cur.next

        while head:
            print head.val
            head = head.next

if __name__ == '__main__':
    head = Node(1)
    tmp = head
    tmp.next = Node(2)
    tmp = tmp.next
    tmp.next = Node(2)
    tmp = tmp.next
    tmp.next = Node(3)
    tmp = tmp.next
    tmp.next = Node(1)
    tmp = tmp.next
    tmp.next = Node(2)
    tmp = tmp.next
    answer = Solution()
    print answer.remove(head)

