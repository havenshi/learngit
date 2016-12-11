LIST = [1, [2, [3, 4], 5], 6, [7, 8]]

def layer_sum(L,layer=1,map = {}):
    for i in range(len(L)):
        if type(L[i])==type(1):
            if layer in map:
                map[layer]+=L[i]
            else:
                map[layer]=L[i]
        else:
            layer_sum(L[i],layer+1)

    return sum([i*map[i] for i in map.keys()])

print layer_sum(LIST)