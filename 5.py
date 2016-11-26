# 5.The output characters of the odd location of the string

# method 1
a= "12345"
print "".join([a[i] for i in range(len(a)) if i%2==0])

print ( ''.join([ c for i, c in enumerate(a) if i % 2 == 0]) )  # i is list[0, 1, 2, 3, 4], c is ['1', '2', '3', '4', '5']
print ( ''.join([ str(i) for i, c in enumerate(a) if i % 2 == 0]) )

# method 2
print a[::2]