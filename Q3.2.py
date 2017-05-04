class Stack:
  def __init__(self):
    self.data = []

  def __str__(self):
    return str(self.data)

  def push(self, data):
    self.data.append(data)

  def pop(self):
    if not self.data:
      print 'Can not pop from empty stack!'

    return self.data.pop()

  def min(self):
    min = self.data.pop()
    while self.data:
        item = self.data.pop()
        if min > item:
          min = item
    return min

if __name__ == '__main__':
  s = Stack()
  s.push(2)
  s.push(1)
  s.push(3)
  s.push(4)
  s.push(5)
  print s.min()