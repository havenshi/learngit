class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    l = ListNode(0)
    cur = l
    for i in range(1,10+1):
        cur.next = ListNode(i)
        cur = cur.next
        print cur.val