class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if root.item > data:
            root.left = self.rinsert(root.left, data)
        elif root.item < data:
            root.right = self.rinsert(root.right, data)
        return root

    def serch(self, data):
        return self.rserach(self.root, data)

    def rserach(self, root, data):
        if root is None or root.item == data:
            return root
        if root.item > data:
            return self.rserach(root.left, data)
        else:
            return self.rserach(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)

    def min_value(self, root):
        current = root
        while current.left is not None:
            current = root.left
        return current

    def max_value(self, root):
        current = root
        while current.right is not None:
            current = root.right
        return current

    def delete(self, data):
        self.root = self.rdelete(self.root, data)

    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.left:
            root.left = self.rdelete(root.left, data)
        elif data > root.right:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.rdelete(root.right, root.item)
        return root

    def size(self):
        return len(self.inorder())
