# moveing nodes and pointers
#


class LRUCache:  # create LRUCache class
    """
    Our LRUCache class keeps track of:

    - the max number of nodes it can hold, (limit = max number?)

    -the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as

    - a storage dict that provides fast access
    to every node stored in the cache.


    trevor:

    DLL = ('item1', 'a')

    storage_dict = { user-input_value : pointer_to_DLL_node }
    {('item1', 'a') : self.dll.head}


    """

    # constructor method (function)
    def __init__(self, limit=10):
        # attributes
        self.limit = limit  # the max number of nodes it can hold
        self.current_size = 0  # the current number of nodes it holds
        # doubly-linked list holds key-value entries in correct order
        self.dll_storage = DoublyLinkedList()
        # Hash Table?
        # storage_dict provides fast access to every node stored in cache
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key.

    Also needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.

    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # either way value is set to head of DLL
        # but to conserve memory, this is done
        # separately at each option

        # # 1. check storage-dict
        #     # if "hit"
        #     # 2. if query is in cache
        #     ???
        #     search for key in object dictionary...
        #     # (set function?)
        #     set(key, value, preexisting)
        #     # 2.1 move node (queary and value) to head of DLL
        #     # 2.1 return value
        #     return value
        #
        #     if "mis"
        #     pass
        #     # 3. if query is NOT in cache
        #     # 3.1 get value from long term memory
        #     ???
        #     search for key in long term memory
        #     # for 3 see set function
        #     set(key, value, preexisting)
        #     # 3.2 set query and value to new head node
        #         # check to see if old node needs to be deleted
        #     # 3.3 return value
        #     return value
        pass

    """
    Adds the given key-value pair to the cache.
    The newly-added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # add to DLL first
        self.dll_storage.add_to_head(value)

        # add to storage dictionary
        # this sets the value of the input as they key
        # of the storage dictionary, with the key of the
        # storage dictionary being a link to the node
        #
        self.storage_dict[key, value] = self.dll_storage.head

        # increment current_size
        self.current_size += 1

        # # update and
        # # overwrite...
        # if key exists but value is different...
        # then overwrite the value?

        # # # if current head:
        # # if (preexisting == True) and ():
        # #     # do nothing
        # #     pass

        #
        # # 1. check how much empty cache space remains
        # # check how many slots are empty in the cache
        # # if remainign space is zero
        #     # pop off the tail
        # # if: the current size is the max size
        # # i.e. no room left
        # if self.current == self.limit:
        #     # then pop off the tail
        #     # i.e. make room
        #     # by getting ride of the least
        #     # recently used item
        #     self.remove_from_tail()
        #
        # else:
        #     #increiment current-counter
        #     self.current += 1
        #
        #     # if value already exists in cache...
        #     # it must be deleted before it is
        #     # again added to the head
        #
        #     #check somehow for pre-exisint
        #     if  True:
        #         # make a copy
        #         saved_copy = node
        #         # delete it first, freeing up space
        #         node.delete()
        #         # make that node the new head
        #         add_to_head(saved_copy)
        #
        #     # 3.2 set query and value to new head node
        #     # check to see if old node needs to be deleted
        #     # check to see size of the new entry?
        #     else preexisting == False:
        #         self.add_to_head({key:value})

        # # add a check?
        # # return True for sucess, False for fail?
        # # check if input # current head?
        # return self.head.value == value
        # pass

        return None
