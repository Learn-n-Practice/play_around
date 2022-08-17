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
        Insert new node as the head of linkedlist
        """
        node.next = self.head
        self.head = node
    
    def insert_last(self, node):
        """
        Insert node to the end of linkedlist
        """
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def insert_after(self, target_node_data, new_node):
        """
        Insert new node after a target node in a linkedlist
        """
        if self.head is None:
            raise Exception("Linkedlist is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found")
 
    def insert_before(self, target_node_data, new_node):
        """
        Insert new node before a target node in a linkedlist
        """
        if self.head is None:
            raise Exception("Linkedlist is empty")

        if self.head.data == target_node_data:
            self.insert_first(new_node)
            return 

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("Linkedlist is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def __iter__(self):
        """
        Make the linkedlist iterable
        """
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