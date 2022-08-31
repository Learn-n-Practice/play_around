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

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        else:
            print(f"Traversal type {traversal_type} is not supported")
            return False

    def preorder_traversal(self, start, traversal):
        """
        Traverse tree in preorder fashion.
        Root->Left->Right
        """
        if start:
            traversal += str(start.value) + " -> "
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        """
        Traverse tree in inorder fashion.
        Left->Root->Right
        """
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.value) + " -> "
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        """
        Traverse tree in postorder fashion.
        Left->Right-Root
        """
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal = self.inorder_traversal(start.right, traversal)
            traversal += str(start.value) + " -> "
        return traversal


if __name__ == "__main__":
    tree = BinaryTree(11)
    n1 = Node(8)
    n2 = Node(9)
    tree.root.left = n1
    tree.root.right = n2
    n11 = Node(5)
    n12 = Node(7)
    n21 = Node(4)
    n22 = Node(3)
    n1.left = n11
    n1.right = n12
    n2.left = n21
    n2.right = n22

    print("Preorder: " + tree.print_tree("preorder"))  # Preorder traversal
    print("Inorder: " + tree.print_tree("inorder"))  # Inorder traversal
    print("Postorder: " + tree.print_tree("postorder"))  # Postorder traversal
