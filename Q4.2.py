def hasRoute(node1, node2):
    if not node1 or not node2:
        return False

    queue = [node1]
    while queue:
        tmp = []
        for node in queue:
            if node == node2:
                return True
            for eachnode in node.adjacent:
                tmp.append(eachnode)
        queue = tmp
    return False
