class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front element:", queue.peek())  # Output: Front element: 1
print("Queue size:", queue.size())  # Output: Queue size: 3

queue.dequeue()
print("Front element after dequeue:", queue.peek())  # Output: Front element after dequeue: 2
print("Queue size after dequeue:", queue.size())  # Output: Queue size after dequeue: 2

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False

queue.dequeue()
queue.dequeue()
print("Is queue empty after dequeuing all elements?", queue.is_empty())  # Output: Is queue empty after dequeuing all elements? True