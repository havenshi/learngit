# Py

n=2992
def py(n,m):
    total = 0
    while n>0:
        total+=n%m
        n=n/m
    return total
print py(n,10)==py(n,16)==py(n,12) and "Yes" or "No"