def distance(array, a, b): # O(n) time, O(1) space.
    n = len(array)
    pos1, pos2 = n-1, n-1
    min = n-1
    for i in range(n):
        if array[i] == a:
            pos1 = i
            if abs(pos1 - pos2) < min:
                min = abs(pos1 - pos2)
        if array[i] == b:
            pos2 = i
            if abs(pos1 - pos2) < min:
                min = abs(pos1 - pos2)

def distance2(array, a, b): # O(nlogn) time.
    n = len(array)
    map = {a:[], b:[]}
    for i in range(n):
        if map[i] == a:
            map[a].append(i)
        if map[i] == b:
            map[b].append(i)
    arraya = map[a]
    arrayb = map[b]
    min = abs(arrayb[0] - arraya[0])
    for i in range(len(arraya)):
        submin = abs(arrayb[0] - arraya[i])
        for j in range(len(arrayb)):
            if abs(arrayb[j] - arraya[i]) < submin:
                submin = abs(arrayb[j] - arraya[i])
        if submin < min:
            min = submin
    return min