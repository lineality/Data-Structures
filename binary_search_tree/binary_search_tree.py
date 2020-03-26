import sys

sys.path.append("../queue_and_stack")
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value_input):

        # if  new < node.value
        # "value" = root node
        if value_input < self.value:
            # go left (lower)

            # if self.left is none: there no branch there
            # so make a new branch
            if self.left == None:
                # if there is no branch: add a new one
                self.left = BinarySearchTree(value_input)

            # if there is a branch keep going
            else:
                self.left.insert(value_input)

        # yes: maybe thie should/could be 'else'?
        elif value_input >= self.value:
            # go right (higher)

            # if self.left is none: there no branch there
            # so make a new branch
            if self.right == None:
                # if there is no branch: add a new one
                self.right = BinarySearchTree(value_input)

            # if there is a branch keep going
            else:
                self.right.insert(value_input)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if root is the target
        if self.value == target:
            return True

        # find the end of the tree
        # run search again on left or right branch
        # if larger or smaller
        else:
            # if smallerer
            if target < self.value:
                # if branch ends: output false, not found
                if self.left == None:
                    return False
                # if branch continues
                # keep looking
                else:
                    return self.left.contains(target)

            # if biggger
            elif target >= self.value:
                # if branch ends: output false, not found
                if self.right == None:
                    return False
                # if branch continues
                # keep looking
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is no right
        if self.right == None:
            return self.value

        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a *recursive or iterative approach
    #
    # for_each performs a traversal of every node in the tree,
    # executing the passed-in callback function on each tree node value.
    #
    # (depth and breadth on day 2)
    def for_each(self, cb):
        # # if the root is empty
        # if self.value == None:
        #     return False

        # run callback function
        # on the current cell
        cb(self.value)

        # if branches exist, check both
        # check each branch
        # if there is no branch
        # don't follow it

        # check left
        if self.left == None:
            pass
        else:
            self.left.for_each(cb)

        # check right
        if self.right == None:
            pass
        else:
            self.right.for_each(cb)

    # # DAY 2 Project -----------------------

    def print_all(self):
        return self.for_each(print)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if node == None:
            return None
        self.in_order_print(node.left)
        # print that lowest left
        print(node.value)
        self.in_order_print(node.right)

        # if node == None:
        #     return None
        # self.in_order_print(node.left)
        # # print that lowest left
        # print(node.value)
        # self.in_order_print(node.right)

        # # look left
        # if self.left != None:
        #     # if left brach exists: go left
        #     self.in_order_print(self.left)
        # # print that lowest left
        # print(self.value)
        # # if no left, look right
        # if self.right != None:
        #     # if right exists, go right
        #     self.in_order_print(self.right)
        # # then repeat

    # Print the value of every node, starting with the given node,
    # in an iterative
    # breadth first traversal
    #
    # Level by level
    def bft_print(self, node):
        # make quququ
        # add root
        # while not empty
        # print
        # add children of node to queue

        # # create a queue
        q = Queue()
        # enqueue firts item
        q.enqueue(node)

        # while not empty
        while q.len() > 0:
            temp = q.dequeue()
            print(temp.value)
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)

        # print
        # add children of node to queue

        # print(self.value)

        # if self.left:
        #   self.bft_print(self.left)

        # if self.right:
        #   self.bft_print(self.left)

        # # print the first node (root)
        # print(self.value)

        # while True:
        #     # if right branch exists
        #     if self.right != None:
        #         # print its value
        #         print(self.right.value)

        #     # if right branch exists
        #     if self.left != None:
        #         # print its value
        #         print(self.left.value)
        #     break

    # Print the value of every node, starting with the given node,
    # in an iterative
    # depth first traversal
    def dft_print(self, node):

        # not recursive? or iterative?
        # Step 1: make a stack
        # Step 2: add parent to stack
        #
        # while: Repeat steps 3 and 4
        # Step 3: remove that parent from stack
        #         print value when removed
        # Step 4: add that parent's children to the stack
        #         go left to right by convention
        #

        # Step 1: make a stack
        dft_stack = Stack()
        # Step 2: add parent to stack
        dft_stack.push(node)

        while dft_stack.len() > 0:
            # Step 3: remove that parent from stack
            temp = dft_stack.pop()
            print(temp.value)
            # Step 4: add that parent's children to the stack
            #         go left to right by convention
            if temp.left:
                dft_stack.push(temp.left)
            if temp.right:
                dft_stack.push(temp.right)
            # Repeat steps 3 and 4

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
