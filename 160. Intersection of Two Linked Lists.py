# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        tmpa = headA
        tmpb = headB
        counta = 0
        taila = None
        while tmpa:
            taila = tmpa
            counta += 1
            tmpa = tmpa.next
        countb = 0
        tailb = None
        while tmpb:
            tailb = tmpb
            countb += 1
            tmpb = tmpb.next
        if taila != tailb or not headA or not headB:
            return
        step = abs(countb - counta)
        if counta > countb:
            while step > 0:
                headA = headA.next
                step -= 1
        else:
            while step > 0:
                headB = headB.next
                step -= 1
        print headA.val
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    b = ListNode(2)
    answer = Solution()
    print answer.getIntersectionNode(a, b)