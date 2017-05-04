def add(a, b):
    if b == 0:
        return a
    sum = a ^ b # 不考虑进位的加法，只有为相异（（0,1）或（1,0））时，结果为1
    carry = a & b << 1 # 只考虑进位，只有都为1时，结果为1并向左移一位
    return add(sum, carry)

def add2(a, b):
    while b != 0:
        sum = a ^ b
        carry = a & b << 1
    return a