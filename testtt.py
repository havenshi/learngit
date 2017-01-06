# -*- coding: utf-8 -*-
def opOrder(op1,op2):  # 当新元素是)，或者stack里的元素优先度高
    order_dic = {'*':3,'/':3,'+':2,'-':2}
    if op1 == '(' or op2 == '(':
        return False
    elif op2 == ')': # 此时需要把)之前的符号pop出来
        return True
    else:
        if order_dic[op1] < order_dic[op2]:
            return False
        else:
            return True # )之前的较高优先度的符号pop出来
def infixToPrefix(string):
    string=string.split()
    prefix = ''
    stack = []
    string_tmp = ''
    for s in string[::-1]:
        if s == '(':
            string_tmp += ')'
        elif s == ')':
            string_tmp += '('
        else:
            string_tmp += s    # reverse string
    for s in string_tmp:
        if s.isalpha():
            prefix = s + prefix  # 往前加
        else:
            while len(stack) and opOrder(stack[-1],s): # stack里有元素，且优先度较高，则加入prefix之前
                op = stack.pop()
                prefix = op + prefix
            if len(stack) == 0 or s != ')': # 只要不是)的符号都往里加
                stack.append(s)
            else:                           # 如果stack有元素(，且s为),pop
                stack.pop()
    if len(stack):
        prefix = ''.join(stack) + prefix
    return " ".join(prefix)

print(infixToPrefix("A * B + C * D"))
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G ) - H * I"))
print(infixToPrefix("( A + B ) * ( C + D + D )"))
print(infixToPrefix("A + B + C + D"))
print(infixToPrefix("A + B + C * D"))