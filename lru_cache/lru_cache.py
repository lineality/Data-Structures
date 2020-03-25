# moveing nodes and pointers
#
import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class LRUCache:  # create LRUCache class

    # constructor method (function)
    def __init__(self, limit=10):
        # attributes
        self.limit = limit  # the max number of nodes it can hold
        self.size = 0  # the current number of nodes it holds
        # doubly-linked list holds key-value entries in correct order
        self.order = DoublyLinkedList()
        # Hash Table (python dict is a hash table)
        # storage_dict provides fast access to every node stored in cache
        self.storage = {}

    def get(self, key):
        # Key is not in cache -- return none
        if key not in self.storage:
            return None

        else:
            # key is in cache

            # move it to most recently used
            node = self.storage[key]
            self.order.move_to_end(node)

            # key value tuple
            return node.value[1]

    # so... both key and value need to be in the DLL
    def set(self, key, value):

        # if item exists (already)
        if key in self.storage:
            # overwrite the value
            node = self.storage[key]
            node.value = (key, value)
            # move to tail (most recently used)
            self.order.move_to_end(node)
            return

        # size is at limit
        if len(self.order) == self.limit:
            # evict the oldest one
            # the oldest is the tail
            index_of_oldest = self.order.head.value[0]
            del self.storage[index_of_oldest]
            self.order.remove_from_head()
            # add the new one to the end

        # add to order
        self.order.add_to_tail((key, value))
        # add to storage
        self.storage[key] = self.order.tail
