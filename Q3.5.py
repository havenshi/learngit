class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class myqueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isEmpty(self):
        return self.stack1 == [] and self.stack2 == []

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        while not self.stack1.isEmpty():
            item = self.stack1.pop()
            self.stack2.push(item)
        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()

if __name__ == '__main__':
    q = myqueue()
    q.enqueue(1)
    q.enqueue(2)
    print q.dequeue()
    print q.dequeue()