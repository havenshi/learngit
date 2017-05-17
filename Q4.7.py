def subtree(T1, T2):
    if not T1 or not T2:
        return False
    if T1.val == T2.val:
        if judge(T1, T2):
            return True
    return subtree(T1.left, T2) or subtree(T1.right, T2)

def judge(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val == t2.val:
        return judge(t1.left, t2.left) and judge(t1.right, t2.right)
    return False