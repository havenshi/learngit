def pair(array, target):
    map = {}
    result = []
    for i in range(len(array)):
        if target - array[i] not in map:
            map[target - array[i]] = array[i]
        else:
            result.append([target - array[i], array[i]])