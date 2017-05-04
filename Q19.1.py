def swap(a, b):
    a = a^b
    b = a^b
    a = a^b

def swap2(a, b):
    b = a-b
    a = a-b
    b = a+b