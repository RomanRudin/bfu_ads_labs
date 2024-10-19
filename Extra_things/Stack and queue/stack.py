



#! IN NEED OF TESTING AND REFACTORING



class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)