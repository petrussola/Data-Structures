# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?

        # -> Because LLs are O(1) inserting and deleting nodes from head and tail. And that is what a queue is about:
        # adding values to head and removing from tail

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            value = self.storage.tail.value
            self.storage.remove_from_tail()
            return value

    def len(self):
        return self.size
