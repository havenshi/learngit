# -*- coding:utf8 -*-
class Stack:
  def __init__(self):
    self.data = []

  def __str__(self):
    return str(self.data)

  def append(self, data):
    self.data.append(data)
    return self.data[-1]

  def pop(self):
    if not self.data:
      print 'Can not pop from empty stack!'

    return self.data.pop()

  def peek(self):
    if not self.data:
      print 'Can not peek empty stack!'

    return self.data[-1]

  def sort(self):
    if not self.data:
      print 'Can not sort on empty stack!'

    tmpstack = Stack()

    while self.data:
      tmp = self.data.pop()
      # 当临时栈里面顶部的元素>tmp，需要将'所有'这种较大顶部元素出栈，加到原栈里面
      while tmpstack.data and tmpstack.peek() > tmp:
        self.data.append(tmpstack.pop())
      tmpstack.append(tmp) # tmp一定会加到临时栈里面

    self.data = tmpstack

if __name__ == '__main__':
  s = Stack()
  s.append(2)
  s.append(1)
  s.append(3)
  s.append(4)
  s.append(5)
  s.sort()
  print s