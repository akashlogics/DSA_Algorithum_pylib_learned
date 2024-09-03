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
        print()
        print("Preorder")
        self.preorder(self.root)
        print()
        print("Postorder")
        self.postorder(self.root)
        print()
        print("levelorder")
        self.levelorder(self.root)
        print()
        print("zigzagorder")
        self.zigzagorder(self.root)
        print()

    def inorder(self, node):#LPR
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")
    def levelorder(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return
    def zigzagorder(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.pop(0)
                print(temp.data, end=" ")
                if i & 1:
                    if temp.right:
                        queue.append(temp.right)
                    if temp.left:
                        queue.append(temp.left)
                else:
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
        return

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


