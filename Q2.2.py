class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def nth(head, n):

    tmp = head
    count = 0
    while count < n:
        tmp = tmp.next
        count += 1

    tmp2 = head
    while tmp:
        tmp = tmp.next
        tmp2 = tmp2.next
    return tmp2.val


# recursion
class Solution(object):
    def __init__(self, node, k):
        self.head = node
        self.k = k
        self.xxx = None

    def nth2(self, head):
        if head.next:
            self.nth2(head.next)
        if self.k == 1:
            self.xxx = head.val
        self.k -= 1

head = Node(1)
tmp = head
tmp.next = Node(2)
tmp = tmp.next
tmp.next = Node(3)
# print nth(head, 2)
answer = Solution(head, 2)
print answer.xxx
print answer.k
answer.nth2(head)
print answer.k
print answer.xxx