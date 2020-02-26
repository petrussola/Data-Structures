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
        
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)


    def contains(self, target):
        next_node = None
        # if there is no root, return False
        # if root == target, return root.value
        if target == self.value:
            return self.value
        elif not self.value:
            return False
        else:
            if target < self.value:
                next_node = self.left
            else:
                next_node = self.right

        def check(node, target):
            if node.value == target:
                return node.value
            elif target < node.value:
                next_node
            else:
                if target < self.value:
                    if self.left:
                        next_node = self.left
                        return check(next_node, target)
                    else:
                        return False
                else:
                    if self.right:
                        next_node = self.right
                        return check(next_node, target)
                    else:
                        return False
        return check(self, target)

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
