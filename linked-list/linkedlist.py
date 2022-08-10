class Node:
    """
    A class that implements a node of a linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    """
    A class that implements a linked list data structure
    """
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(data=item)
                node = node.next

    def insert_first(self, node):
        """
        Insert new node as the head of linked list
        """
        node.next = self.head
        self.head = node
    
    def insert_last(self, node):
        """
        Insert node to the end of linked list
        """
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)