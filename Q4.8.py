# -*- coding:utf-8 -*-
# 有父结点指针
def sumtree(root, x):
    result = []
    dfs(root, x, result)
    return result

def dfs(root, x, result):
    tmp = [root.val]
    if sum(tmp) == x:
        result.append(tmp[::-1])
    while root.parent:
        root = root.parent
        tmp.append(root.val)
        if sum(tmp) == x:
            result.append(tmp[::-1])
    dfs(root.left, x, result) and dfs(root.right, x, result)

# 没有父结点
def sumtree2(root, x):
    result = []
    dfs2(root, x, result, tmp = [])
    return result

def dfs2(root, target, result, tmp):
    if not root:
        return
    if root.val == target:
        result.append(tmp + [root.val])
    dfs2(root.left, target, result, []) # start from left
    dfs2(root.right, target, result, [])  # start from right
    dfs2(root.left, target - root.val, result, tmp + [root.val]) # already add root.val, continue to its left
    dfs2(root.right, target - root.val, result, tmp + [root.val])  # already add root.val, continue to its right
