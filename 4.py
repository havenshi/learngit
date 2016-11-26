# 4.Output the dictionary keys

a={1:1,2:2,3:3}

# method 1
print ",".join([str(i) for i in a.keys()])    # attention! join string! a.keys() is a list

# method 2
print ",".join(map(str, a.keys()))   # map(func, list)