class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_helper(self.root, data)

    def _insert_helper(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
            else:
                self._insert_helper(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = TreeNode(data)
            else:
                self._insert_helper(current.right, data)
        else:
            print('Value already in tree')

    def printtree(self):
        print("Inorder")#LPR
        self.inorder(self.root)
        print("Preorder")

    def _print_helper(self, node):
        if node:
            self._print_helper(node.right)
            print(node.data)
            self._print_helper(node.left)

            #print("Preorder")#PLR
            #print(node.data)
            #self._print_helper(node.left)
            #self._print_helper(node.right)
#
            #print("Postorder")#LRP
            #self._print_helper(node.left)
            #self._print_helper(node.right)
            #print(node.data)

# Create an instance of BST and insert some values
t = BST()
t.insert(50)
t.insert(30)
t.insert(20)
t.insert(40)
t.insert(70)
t.insert(60)
t.insert(80)

# Print the tree
t.printtree()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_helper(self.root, data)

    def _insert_helper(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
            else:
                self._insert_helper(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = TreeNode(data)
            else:
                self._insert_helper(current.right, data)
        else:
            print('Value already in tree')

    def printtree(self):
        print("Inorder")
        self.inorder(self.root)
        print("Preorder")
        self.preorder(self.root)
        print("Postorder")
        self.postorder(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

# Create an instance of BST and insert some values
t = BST()
t.insert(50)
t.insert(30)
t.insert(20)
t.insert(40)
t.insert(70)
t.insert(60)
t.insert(80)

# Print the tree
t.printtree()