# create a linked list
# head=ListNode(0)
# cur=head
# for i in range(5):
#     node=ListNode(i)
#     cur.next=node
#     cur=cur.next
# print head.next.val
# print head.next.next.next.val
# print head.next.next.next.val
# Definition for singly-linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


        res = ListNode(0)
        res.next = head
        tmp = res                    # head 1-5, tmp0-5
        for i in range(0, n):        # double pointer, a.head from 1 to None is 5 steps, forward 2. This means the 1st pointer firstly complete n steps. Then together with 2nd pointer, complete (total -n) steps will come to the node which will be removed.
            head = head.next
        while head != None:          # b.tmp from 0 to 5 is also 5 steps, 5-2=3(how many steps left for head), point tmp to the nth node
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next


