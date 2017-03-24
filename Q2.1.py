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
            tmp = cur.next
            while tmp:
                if tmp.val == cur.val:
                    cur.next = cur.next.next
                    tmp = cur.next
                else:
                    tmp = tmp.next
            cur = cur.next

        while head:
            print head.val
            head = head.next

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head = head.next
    head.next = Node(2)
    head = head.next
    head.next = Node(3)
    head = head.next
    head.next = Node(1)
    head = head.next
    head.next = Node(2)
    head = head.next
    answer = Solution()
    print answer.remove(head)



