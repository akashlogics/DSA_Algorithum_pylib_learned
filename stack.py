class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.peek())  # Output: Top element: 3
print("Stack size:", stack.size())  # Output: Stack size: 3

stack.pop()
print("Top element after pop:", stack.peek())  # Output: Top element after pop: 2
print("Stack size after pop:", stack.size())  # Output: Stack size after pop: 2

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

stack.pop()
stack.pop()
print("Is stack empty after popping all elements?", stack.is_empty())  # Output: Is stack empty after popping all elements? Trueclass Stack: