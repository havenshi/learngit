def circle(head):
    slow = head
    fast = head
    while fast and fast.next:
        if slow.val == fast.val:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        slow = slow.next
        fast = fast.next.next
    return False