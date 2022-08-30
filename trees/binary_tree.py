class Node:
    """
    A class to implements nodes in the binary tree
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    A class which implements a binary tree
    """
    def __init__(self, root):
        self.root = Node(root)