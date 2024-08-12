import pandas as pd
import heapq

class HeapSet:
    def __init__(self):
        self.heap = []
        self.set = set()

    def add(self, value):
        if value not in self.set:
            heapq.heappush(self.heap, value)
            self.set.add(value)

    def remove(self, value):
        if value in self.set:
            self.heap.remove(value)
            heapq.heapify(self.heap)
            self.set.remove(value)

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def __len__(self):
        return len(self.set)

# Usage example
heapset = HeapSet()
heapset.add(5)
heapset.add(3)
heapset.add(7)
heapset.add(3)  # Duplicate value will not be added

print(heapset.peek())  # Output: 3
print(len(heapset))  # Output: 3

heapset.remove(3)
print(heapset.peek())  # Output: 5
print(len(heapset))  # Output: 2