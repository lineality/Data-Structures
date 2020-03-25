import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


# create class
class Queue:
    # constructor
    def __init__(self):
        # attributes
        self.size = 0  # this is manually used
        # A Doubly Linked list is used for a queue
        # because it is dynamic in size and easily
        # performs the operations
        self.storage = DoublyLinkedList()

    # class methods (functions)
    def enqueue(self, value):
        # increment size
        self.size += 1
        # Add a number to the Tail
        self.storage.add_to_tail(value)

    def dequeue(self):
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
