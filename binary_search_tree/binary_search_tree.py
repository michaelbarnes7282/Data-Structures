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
        # compare the input value with the value of the node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            if self.left is None:
            # if we see that there is no left child, then we can wrap
            # the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
                # call the left child's 'insert' method
                self.left.insert(value)
            # if there's no node to compare the input value to,
            # then we can wrap the value in a BST node and park it
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see that there is no right child,
            if self.right is None:
                # then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            else:
                # otherwise there is a child
                # call the right child's 'insert' method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)



    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque

        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            print(current.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        stack = []
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop() 
            if current.right:
                stack.append(current.right)

            if current.left:
                stack.append(current.left)

            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)

