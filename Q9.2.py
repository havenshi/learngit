def anagrams(array):
    map = {}
    for item in array:
        newi = "".join(sorted(item))
        if newi in map:
            map[newi] += [item]
        else:
            map[newi] = [item]
    arraykey = sorted([i for i in map.keys()])
    result = []
    for key in arraykey:
        result += map[key]
    return result
print anagrams(["axyz", "abc", "yzax", "bac", "zyxa", "fg", "gf"])