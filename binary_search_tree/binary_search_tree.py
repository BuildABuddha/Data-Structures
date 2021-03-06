"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # Check left side
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            # Check right side
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            # Found value! Return True!
            return True

        elif target < self.value:
            # Check left side
            if self.left is None:
                # Dead end! Return False!
                return True
            else:
                # Go deeper...
                return self.left.contains(target)

        elif target > self.value:
            # Check right side
            if self.right is None:
                # Dead end! Return false!
                return False
            else:
                # Go deeper...
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value
        current_node = self.right

        while current_node:
            if current_node.value > max_val:
                max_val = current_node.value
            current_node = current_node.right

        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if not self.left is None:
            self.left.for_each(fn)
        if not self.right is None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Why does this need to have a node as the input? Ah well.
        if not node.left is None:
            node.left.in_order_print(node.left)

        print(node.value)

        if not node.right is None:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node_queue = [node]

        while node_queue:
            current_node = node_queue.pop(0)  # We don't need to import in a queue if we just do this.
            print(current_node.value)

            if not current_node.left is None:
                node_queue.append(current_node.left) 
             
            if not current_node.right is None:
                node_queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)

        if not node.left is None:
            node.left.dft_print(node.left)

        if not node.right is None:
            node.right.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Same as dft_print function
        self.dft_print(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if not node.left is None:
            node.left.post_order_dft(node.left)

        if not node.right is None:
            node.right.post_order_dft(node.right)

        print(node.value)
