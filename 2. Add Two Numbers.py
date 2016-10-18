# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i=1
        total=0
        while i<=100:
            a=l1.val
            b=l2.val
            total+=i*(a+b)
            l1=l1.next
            l2=l2.next
            i*=10

        newl=ListNode(total%10)
        total//=10
        newl2 = ListNode(total % 10)
        total //= 10
        newl3 = ListNode(total % 10)
        newl.next = newl2
        newl2.next = newl3
        return [newl.val]+[newl.next.val]+[newl.next.next.val]

if __name__ == "__main__":
    answer = Solution()
    l1 = ListNode(2)
    l12 = ListNode(4)
    l13 = ListNode(3)
    l1.next=l12
    l12.next=l13
    l2 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)
    l2.next=l22
    l22.next=l23
    print answer.addTwoNumbers(l1, l2)

