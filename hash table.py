class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            # Collision resolution using chaining (linked list)
            node = self.table[index]
            while node is not None:
                if node[0] == key:
                    node[1] = value  # Update value if key already exists
                    return
                if node[2] is None:
                    break
                node = node[2]
            node[2] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        while node is not None:
            if node[0] == key:
                return node[1]
            node = node[2]
        return None

# Usage
hash_table = HashTable(10)
hash_table.insert(1, "one")
hash_table.insert(2, "two")
hash_table.insert(3, "three")
hash_table.insert(11, "eleven")

print(hash_table.get(1))  # Output: one
print(hash_table.get(2))  # Output: two
print(hash_table.get(3))  # Output: three
print(hash_table.get(11))  # Output: eleven
print(hash_table.get(4))  # Output: None