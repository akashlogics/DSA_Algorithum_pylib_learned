class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# Example usage of a binary tree

# Create nodes
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)
child4 = TreeNode(5)

# Add children to the root node
root.add_child(child1)
root.add_child(child2)

# Add children to child1
child1.add_child(child3)
child1.add_child(child4)

# Traverse the tree (Depth-First Search)
def traverse_tree(node):
    print(node.value)
    for child in node.children:
        traverse_tree(child)

# Traverse the binary tree
traverse_tree(root)