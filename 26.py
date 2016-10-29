# Sequence to judge

L=[1,2,3,4]
print("UP" if L==sorted(L) else "DOWN" if L==sorted(L)[::-1] else "WRONG" )