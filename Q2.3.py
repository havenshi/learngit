#-*- coding:utf8 -*-
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def middle(head):
    if not head or not head.next: # 没有或只有1个node的情况
        return head
    slow = head
    fast = head
    pre = None
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    # 如果slow在中部
    if slow.next:
        tmp = slow.next.val
        slow.val = tmp
        slow.next = slow.next.next
    # 如果slow已经是尾部，加pre
    else:
        pre.next = None

    tmp2 = head
    while tmp2:
        print tmp2.val
        tmp2 = tmp2.next

head = Node(1)
tmp = head
tmp.next = Node(2)
tmp = tmp.next
tmp.next = Node(3)
tmp = tmp.next
tmp.next = Node(4)
tmp = tmp.next
tmp.next = Node(5)
tmp = tmp.next
tmp.next = Node(6)
print middle(head)
