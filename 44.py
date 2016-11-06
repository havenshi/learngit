# super stairs

def stairs(n):
    return (n==1 or n==2) and 1 or (stairs(n-1)+stairs(n-2))

print(stairs(3))