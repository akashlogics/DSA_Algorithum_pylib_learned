class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                break

            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage of a double linked list

dll = DoubleLinkedList()

dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_end(4)
dll.insert_at_end(5)

dll.display()  # Output: 1 2 3 4 5

dll.delete_node(3)
dll.display()  # Output: 1 2 4 5