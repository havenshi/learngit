# -*- coding: utf-8 -*-
from pythonds.basic.stack import Stack
# 中缀转后缀
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

# 后缀计算
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))


# 中缀转前缀
def opOrder(op1,op2):  # 当新元素是)，或者stack里的元素优先度高
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    if op1 == '(' or op2 == '(':
        return False
    elif op2 == ')': # 此时需要把)之前的符号pop出来
        return True
    else:
        if prec[op1] < prec[op2]:
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

# 前缀计算
def prefixEval(prefixExpr):
    operandStack = Stack()
    tokenList = (prefixExpr.split())[::-1]

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(prefixEval('- * + 1 2 - 8 5 6'))