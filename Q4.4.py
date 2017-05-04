def create(root):
    result = []
    if root:
        result.append(root.val)
        queue = [root]
        while queue:
            tmpq = []
            tmpr = []
            for node in queue:
                if node.left:
                    tmpq.append(node.left)
                    tmpr.append(node.left.val)
                if node.right:
                    tmpq.append(node.right)
                    tmpr.append(node.right.val)
            queue = tmpq
            if tmpr:
                result += tmpr

    head = ListNode(0)
    tmp = head
    for item in result:
        tmp.next = ListNode(item)
        tmp = tmp.next
    return head.next
