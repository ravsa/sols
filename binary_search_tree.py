class Tree:

    def __init__(self):
        self._tree = None

    class Node:

        def __init__(self, key):
            self.data = key
            self.right = self.left = None

    def add_node(self, data):
        if self._tree:
            if self._tree.data <= data:
                if not self._tree.right:
                    self._tree.right = self.Node(data)
                else:
                    self._tree.right = self.add_node(data)
            else:
                if not self._tree.left:
                    self._tree.left = self.Node(data)
                else:
                    self._tree.left = self.add_node(data)

    def inorder(self, tree):
        if tree:
            print tree.data
            self.inorder(tree.left)
            self.inorder(tree.right)

T = Tree()
T.add_node(7)
T.add_node(9)
T.add_node(4)
T.add_node(5)
T.add_node(1)
T.add_node(10)
T.inorder(T._tree)
