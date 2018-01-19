#coding=utf-8

class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    print s1.peek()
    print s1
    print s1.pop()
    print s1
    print s1.is_empty()