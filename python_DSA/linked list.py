class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        if position < 0:
            raise ValueError("Position must be non-negative")
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            raise IndexError("List is empty")
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            raise IndexError("List is empty")
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position < 0:
            raise ValueError("Position must be non-negative")
        if not self.head:
            raise IndexError("List is empty")
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next
        if not current.next:
            raise IndexError("Position out of range")
        current.next = current.next.next

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sorted_lists(self, other_list):
        if not self.head:
            return other_list
        if not other_list.head:
            return self
        merged_list = LinkedList()
        current1 = self.head
        current2 = other_list.head
        while current1 and current2:
            if current1.data < current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next
        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
        return merged_list

    def detect_and_remove_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return
        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

# Usage
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_beginning(0)
list1.insert_at_position(2, 2)
print(list1.display())  # Output: [0, 1, 2, 3, 5]

list1.delete_at_beginning()
list1.delete_at_end()
list1.delete_at_position(1)
print(list1.display())  # Output: [1, 3]

print(list1.search(3))  # Output: 1
print(list1.search(4))  # Output: -1

list1.reverse()
print(list1.display())  # Output: [3, 1]

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
merged_list = list1.merge_sorted_lists(list2)
print(merged_list.display())  # Output: [1, 2, 3, 4, 6]

list3 = LinkedList()
list3.insert_at_end(1)
list3.insert_at_end(2)
list3.insert_at_end(3)
list3.head.next.next.next = list3.head  # Creating a loop
list3.detect_and_remove_loop()
print(list3.display())  # Output: [1, 2, 3]