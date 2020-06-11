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
from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                # print(f"self.right has value: {self.right}")
                self.right.insert(value)
            else:
                # print("self.right has no value")
                self.right = BSTNode(value)
        else:
            if self.left:
                # print(f"self.left has value: {self.left}")
                self.left.insert(value)
            else:
                # print("self.left has no value")
                self.left = BSTNode(value)
        


        # current = self
        # while current.left or current.right:
        #     if current.value > value:
        #         current = current.left
        #     elif current.value < value:
        #         current = current.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            # print(f"self.value: {self.value} == target {target}")
            return True
        elif target > self.value:
            # print(f"self.value: {self.value} > target {target}")
            if self.right:
                return self.right.contains(target)
        elif target < self.value:
            # print(f"self.value: {self.value} < target {target}")
            if self.left:
                return self.left.contains(target)
        else:
            return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        
        '''Guided project solution
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        '''
    def iter_depth_first_for_each(self, fn):
        stack = []

        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            fn(self.value)
    
    def breadth_first_for_each(self, fn):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current = q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            fn(self.value)

    # Part 2 -----------------------
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

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
