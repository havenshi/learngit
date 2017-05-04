class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def add(node1, node2):
    carry = 0
    new = Node(0)
    newnode = new
    while node1 or node2 or carry:
        tmp = 0
        if node1:
            tmp += node1.val
            node1 = node1.next
        if node2:
            tmp += node2.val
            node2 = node2.next
        if carry:
            tmp += carry
        value = tmp%10
        carry = tmp/10
        newnode.next = Node(value)
        newnode = newnode.next
    return new.next

node1 = Node(3)
tmp = node1
tmp.next = Node(1)
tmp = tmp.next
tmp.next = Node(5)
node2 = Node(5)
tmp2 = node2
tmp2.next = Node(9)
tmp2 = tmp2.next
tmp2.next = Node(2)
result = add(node1, node2)
while result:
    print result.val
    result = result.next