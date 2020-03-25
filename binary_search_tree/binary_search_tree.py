# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


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
                self.left = BinarySearchTree(value_input)

            # if there is a branch keep going
            else:
                self.left.insert(value_input)

        if value_input >= self.value:
            # go right (higher)

            # if self.left is none: there no branch there
            # so make a new branch
            if self.right == None:
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
            if target >= self.value:
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
    # There is myriad ways to perform tree traversal;
    # in this case any of them should work.
    #
    # depth and breadth
    # Call the function `cb` on the value of each node
    # You may use a *recursive or iterative approach
    #
    # for_each performs a traversal of every node in the tree,
    # executing the passed-in callback function on each tree node value.
    #
    # depth and breadth
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

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
