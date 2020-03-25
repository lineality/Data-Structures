import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Stack:  # make class
    # constructor method (function, but shhhh...don't call it a function)
    def __init__(self):
        # attributes:
        self.size = 0
        # A Doubly Linked list is used for a stack
        # because it is dynamic in size and easily
        # performs the operations
        self.storage = DoublyLinkedList()

    def push(self, value):

        # incriment size
        self.size += 1
        # Add a number to the Tail
        self.storage.add_to_head(value)

    def pop(self):
        if self.len() == 0:
            # return "Queueue Is Emptyie"
            pass
        else:
            # decriment size
            self.size -= 1
            # step 1: print the last item in queue (the head)
            output = self.storage.head.value
            # step 2: delete the last item in queue (the head)
            self.storage.remove_from_head()
            return output

    def len(self):
        # return the length of the queue
        # return self.storage.length
        return self.size
