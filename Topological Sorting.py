from collections import deque


def kahn_topsort(graph):
    in_degree = {u: 0 for u in graph}  # determine in-degree
    for u in graph:  # of each node
        for v in graph[u]:
            in_degree[v] += 1
    # in_degree = {'wash laundry': 0, 'cook food': 0, 'dry laundry': 1, 'have lunch': 2, 'fold laundry': 1, 'wash the dishes': 0}

    Q = deque()  # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
    # Q = deque(['wash the dishes', 'cook food', 'wash laundry']), find all initial nodes

    L = []  # list for order of nodes
    while Q:
        u = Q.pop()  # choose node of zero in-degree
        L.append(u)  # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)
    # L = ['wash laundry', 'cook food', 'wash the dishes', 'dry laundry', 'have lunch', 'fold laundry']

    if len(L) == len(graph):
        return L
    else:  # if there is a cycle,
        return []  # then return an empty list


graph_tasks = { "wash the dishes" : ["have lunch"],
                "cook food" : ["have lunch"],
                "have lunch" : [],
                "wash laundry" : ["dry laundry"],
                "dry laundry" : ["fold laundry"],
                "fold laundry" : [] }
order = kahn_topsort(graph_tasks)

for task in order:
    print(task)