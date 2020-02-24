# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because we remove from head al the time, and LL are very fast at
        # it
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -= 1
        value = self.storage.head.value
        self.storage.remove_from_head()
        return value

    def len(self):
        return self.size
