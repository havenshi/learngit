# -*- coding:utf-8 -*-
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head == None: return None
        tmp = head
        while tmp:         # 首先，在原链表的每个节点后面都插入一个新节点，新节点的内容和前面的节点一样。1后面插入1，2后面插入2，依次类推。
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next

        tmp = head
        while tmp:   # 其次，原链表中的random指针如何映射呢？1节点的random指针指向3，则它的映射1的random指向原来1的random的映射。
            if tmp.random:
                tmp.next.random = tmp.random.next # ！！！
            tmp = tmp.next.next

        newhead = head.next  # 从1的映射开始
        pold = head
        pnew = newhead
        while pnew.next:    # 第三步，将新的链表从上图这样的链表中拆分出来。pold和pnew两个指针交替进行。
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead