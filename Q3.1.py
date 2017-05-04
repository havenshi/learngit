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


if __name__ == '__main__':
  nums = [1,2,3]
  i = len(nums)/3
  num1 = nums[:i]
  num2 = nums[i:2*i]
  num3 = nums[2*i:]
  s1 = Stack()
  s2 = Stack()
  s3 = Stack()
  for i in range(len(num1)):
    s1.push(num1[i])
  for i in range(len(num2)):
    s2.push(num2[i])
  for i in range(len(num3)):
    s3.push(num3[i])

  print s1,s2,s3