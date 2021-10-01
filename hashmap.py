from LinkedListAndTree import Node


def alphInt(char):
    """
    Returns the position of any letter within the alphabet.

    Returns:
        int: The position of any 'char' character within the alphabet. Ranges from 1 - 26.

    Notes:
        Yes, this docstring IS pointless, but consistency is important.
    """
    return ord(char.lower()) - 96


class hashIter:
    """
    Acts as the iterator for the 'hasMap' class.

    Attributes:
        index (int): The index of the 'keys' list to be returned when the '__next__' method is called. Reset to 0 once iteration ends.

        keys (list): A list of hash map keys from a 'hashMap' object.__base__

    Methods:
        __init__(self, keys)

        __next__(self)
    """

    def __init__(self, keys):
        self.index = 0
        self.keys = keys


    def __next__(self):
        """
        Used to iterate over the contents of a hash map.

        Returns:
            current (str): The 'current' key during each cycle of iteration. 

        Raises:
            StopIteration: A 'StopIteration' exception is raised on the '.index' attribute has exceeded the length of the '.keys. list. '.index' is reset to 0.
        """
        
        if self.index == len(self.keys):

            self.index = 0
            raise StopIteration

        else:

            current = self.keys[self.index]
            self.index += 1

            return current

class hashMap:
    """
    Represents a hash map data structure. 
    
    Attributes:
        keys (list): A list of every key in a hash map. Every key is automatically added as a string.

        arr (list): A list of 'Node' objects. Each entry within is actually the head node of a linked list, storing either a tuble containing a key and it's paired value,
            or a 'None' object. This useage of empty nodes is done in order to both allow each index to store several keys of the same value index as well as to more easily
            have a list of a fixed size, as arrays in python have no preset sizes and empty spaces.

        count (int): The number of entries present in the hash map. 

    Methods:
        __init__(self, arr, length)

        hashFunc(self, key)

        hashInsert(self, key, value)

        hashSearch(self, key)

        hashDelete(self, key)

        __iter__(self)
    """
    
    def __init__(self, arr=None, length=20):
        """
        Automatically creates the relationship between keys and values based on their position in a given list.

        Arguments:
            arr (list, optional): The list of values given in order to have relationships automatically drawn between its entires within the hash map. Every entry
                at an even index within the list will automatically become a key within the hash map. Every key will be paired with the value at the index equal to 
                its own plus 1. For example, the entry at position 6 of a given list would become a key, while the entry at position 7 would become its paired value.
                The hash map will be left blank if no 'arr' argument is given.

            length (int, optional): The number of entries the '.arr' attribute will have. The maximum index of the '.arr' attribute will be equal to this number minus 1.
        
        Raises:
            Exception: In the event that the list given as the 'arr' argument has an odd number of entries, an exception is raised.
        """

        self.keys = []
        self.arr = [Node(None) for x in range(length)]

        if arr == None:
        
            self.count = 0

        elif len(arr) % 2 == 1:
            raise Exception("The list given as an argument when creating a 'hashMap' object must contain an even number of objects.")

        else:

            self.count = len(arr)//2

            for num in [x for x in range(len(arr)) if x % 2 == 0]:

                key = str(arr[num])
                value = arr[num + 1]
                index = hash(key) % length

                self.keys.append(key)

                if self.arr[index].value == None:
                    self.arr[index] = Node((key, value))

                elif self.arr[index].value[0] == key:
                    self.arr[index] = Node((key, value))

                else:

                    current_node = self.arr[index]

                    while current_node.next != None:

                        if current_node.next.value[0] == key:
                            break

                        current_node = current_node.next

                    current_node.next = Node((key, value))


    def hashInsert(self, key, value):
        """
        Inserts a new entry into the hash map.

        Arguments:
            key (str): The key attached to the entry within the hash map.

            value (no designated type): The value paired with the key.

        Notes:
            When a new entry is made using a previously existed key, the new entry overwrites the pre-existing entry. In the event of a collision between key's indexes, 
                the new entry is appended to the end of the linked list at that specific index.
        """

        index = hash(key) % len(self.arr)

        if self.arr[index].value == None:
            self.arr[index] = Node((key, value))

        elif self.arr[index].value[0] == key:
            self.arr[index] = Node((key, value))

        else:

            current_node = self.arr[index]

            while current_node.next != None:

                if current_node.next.value[0] == key:
                    break

                current_node = current_node.next

            current_node.next = Node((key, value))

        if key not in self.keys:
            self.keys.append(key)
            self.count = len(self.keys)


    def hashSearch(self, key):
        """
        Returns the valued paired with a specific key within the hash map.

        Arguments:
            key (str): The key to have its contents returned.

        Returns:
            (no designated type): The data stored within the hash map alongside the key.

        Raises:
            Exception: In the event that the given 'key' argument matches no key within the hash map, an exception is raised.
        """

        index = hash(key) % len(self.arr)

        try:

            if self.arr[index].value[0] == key:
                return self.arr[index].value[1]

            else:
                
                current_node = self.arr[index]

                while current_node.value[0] != key:
                    current_node = current_node.next

                return current_node.value[1]

        except ValueError or TypeError:
            raise Exception("Provided key has no paired value within 'hashMap' object.")


    def hashDelete(self, key):
        """
        Deletes an entry within the hash map.

        Arguments:
            key (str): The key to the entry to be deleted. Both the key and paired value of the entry will be wiped.

        Raises:
            Exception: In the event that the given 'key' argument matches no key within the hash map, an exception is raised.
        """
        
        index = hash(key) % len(self.arr)

        try:
            self.keys.remove(key)
            self.count = len(self.keys)

            if self.arr[index].value[0] == key:
                self.arr[index] = None

            else:
                    
                current_node = self.arr[index]

                while current_node.next.value[0] != key:
                    current_node = current_node.next

                current_node.next = None
        
        except ValueError or TypeError:
            raise Exception("Provided key has no paired value within 'hashMap' object.")


    def __iter__(self):
        """
        Returns a 'hashIter' object containing the details of the specific hash map calling this method.

        Returns:
            hashIter: The iterator of this hash map object. The iterator is passed all the necessary details through arguments. Only the keys of the hash map are looped over.
        """
        return hashIter(self.keys)
