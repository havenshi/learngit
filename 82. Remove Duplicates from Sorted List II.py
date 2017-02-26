# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        current = head
        previous = None
        prepre = None  # third cursor
        flag = 0
        while current != None:  # test several times
            if previous != None:
                if current.val == previous.val:
                    previous.next = current.next  # remove current
                    current = previous.next
                    flag = 1
                else:  # is previous != current, two states need to be considered
                    if flag == 0:  # move on
                        prepre = previous
                        previous = current
                        current = current.next
                    else:  # also remove previous
                        if prepre != None:
                            prepre.next = current
                            previous = current
                            current = current.next
                        else:
                            previous = None
                            head = current
                        flag = 0
            else:  # previous == None, move on
                previous = current
                current = current.next

        if flag == 1 and head != None:  # if list end but still flag == 1, remove previous
            if prepre != None:
                prepre.next = current
            else:
                head = current

        return head