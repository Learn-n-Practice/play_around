class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_item(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next