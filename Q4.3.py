class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build(array):           # bfs
    if len(array) == 0:
        return
    root = Tree(array[0])
    queue = [root]
    array = array[1:]
    while queue:
        tmp = []
        for node in queue:
            if array:
                node.left = Tree(array[0])
                array = array[1:]
                tmp.append(node.left)
            if array:
                node.right = Tree(array[0])
                array = array[1:]
                tmp.append(node.right)
        queue = tmp

    result = []
    if root:
        result.append([root.val])
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
                result.append(tmpr)
    return result

# print build([1,2,3,4,5,6,7])


def build2(array):           # dfs
    if len(array) == 0:
        return
    root = Tree(array[0])
    array = array[1:]
    mid = len(array)/2
    root.left = build2(array[:mid])
    root.right = build2(array[mid:])
    return root


root = build2([1, 2, 3, 4, 5, 6, 7])
result = []
if root:
    result.append([root.val])
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
            result.append(tmpr)
print result
