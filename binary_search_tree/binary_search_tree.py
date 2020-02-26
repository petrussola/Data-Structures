# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        next_node = None
        if value < self.value:
            next_node = self.left
            if not next_node:
                self.left = BinarySearchTree(value)
        else:
            next_node = self.right
            if not next_node:
                self.right = BinarySearchTree(value)
        while next_node:
            if value < next_node.value:
                if next_node.left:
                    next_node = next_node.left
                else:
                    next_node.left = BinarySearchTree(value)
                    return
            else:
                if next_node.right:
                    next_node = next_node.right
                else:
                    next_node.right = BinarySearchTree(value)
                    return 

        # if value < self.value:
        #     if not self.left:
        #         self.left = BinarySearchTree(value)
        #         return
        #     else:
        #         next_node = self.left
        # else:
        #     if not self.right:
        #         self.right = BinarySearchTree(value)
        #         return
        #     else:
        #         next_node = self.right
        # while next_node:
        #     # go down the tree
        #     if value < next_node.value and next_node.left:
        #         next_node = next_node.left
        #     elif value >= next_node.value and next_node.right:
        #         next_node = next_node.right
        # if value < next_node.value:
        #     next_node.left = BinarySearchTree(value)
        # else:
        #     next_node.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # if there is no root, return False

        # if root == target, return root.value

        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
