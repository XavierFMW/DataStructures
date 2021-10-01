
class queue:
    """
    Represents a queue data structure.

    Attributes:
        arr (list): The array containing all the values in the queue.

        back (int): The index of the last item on the queue.

        frontValue (no designated type): The value stored at the front of the queue, the first item in "arr."

    Methods:
        __init__(self, arr)

        addQueue(self, value)

        removeQueue(self)

        pushQueue(self)

        __iter__(self)

        __next__(self)

    Notes: 
        This object is both iterable and its own iterator, as it contains both the "__iter__" and "__next__" methods and its "__iter__" method returns "self."
    """

    def __init__(self, arr=[]):
        """
        Creates the instance attributes the object needs to function properly.

        Arguments:
            arr (list, optional): The list of values to be stored in the queue, left empty by default.
        """
        self.arr = arr
        self.back = len(arr) - 1

        if len(arr) > 0:
            self.frontValue = self.arr[0]
        
        else:
            self.frontValue = None


    def addQueue(self, value):
        """
        Adds a value to the back of the queue.

        Arguments:
            value (no designated type): The value to be added to the back of the queue.
        """

        self.arr.append(value)
        self.back += 1


    def removeQueue(self):
        """
        Removes the value at the back of the queue.
        """

        self.arr.pop()
        self.back -= 1
  
        
    def pushQueue(self):
        """
        Pushes the queue forward, removes the value at the front of the queue and updates the "frontValue" instance attribute.
        """

        self.arr.pop(0)
        self.back -= 1

        if len(self.arr) == 0:
            self.frontValue = None
        
        else:
            self.frontValue = self.arr[0]


    def __iter__(self):
        """
        Simply returns "self," as the object is its own iterator.

        Returns:
            self (queue): The object given to the "__next__" method is the instance itself, as this object is its own iterator.
        """

        return self


    def __next__(self):
        """
        Used to iterate over the contents of the queue. Returns and remembers one value at a time until the end of the queue is reached.

        Returns:
            current (no desgnated type): The front value of the array within the queue.

        Notes:
            Due to the nature of queue data structures, iterating over the queue from back to front also erases the contents of the queue, as the value at the front must
            be deleted before the next value is analyzed.
        """

        if self.back <= -1:
            raise StopIteration
            
        current = self.frontValue
        self.pushQueue()

        return current


class deque:
    """
    Represents a deque data type.

    Attributes:
        arr (list): The array of values stored within the deque.

        length (int): The index of the last item in the deque. Keep in mind, does not equal the number of items stored.

        leftValue (no designated type): The value at the very beginning of the deque.

        rightValue (no designated type): The value stored at the very end of the deque.

    Methods:
        __init__(self, arr)

        addLeftDeque(self, value)

        removeLeftDeque(self)

        addRightDeque(self, value)

        removeRightDeque(self)

    Notes:
        Unlike the queue and stack data structures in this project, these deques are not iterable, as unlike stacks and queues there is no obvious direction for a 
        deque to iterate towards. Deques have no fronts or backs or tops or bottoms, so iteration was not implemented.
        
    """

    def __init__(self, arr=[]):
        """
        Creates the instance attributes the object needs to function properly.

        Arguments:
            arr (list, optional): The list of values to be stored in the deque, left empty by default.
        """

        self.arr = arr
        self.length = len(arr) - 1

        if len(arr) >= 2:

            self.leftValue = self.arr[0]
            self.rightValue = self.arr[-1]

        elif len(arr) == 1:
            self.leftValue = self.arr[0]
            self.rightValue = self.arr[0]
        
        else:
            self.leftValue = None
            self.rightValue = None


    def addLeftDeque(self, value):
        """
        Adds to the left side (beginning) of the deque.

        Arguments:
            value (no designated type): The value to be added to the left of the deque.
        """

        self.arr.insert(0, value)
        self.leftValue = value
        self.length += 1

        if self.rightValue == None:
            self.rightValue = value


    def removeLeftDeque(self):
        """
        Removes from the left side (beginning) of the deque.
        """

        self.arr.pop(0)
        self.length -= 1

        if len(self.arr) == 0:

            self.leftValue = None
            self.rightValue = None

        else:
            self.leftValue = self.arr[0]


    def addRightDeque(self, value):
        """
        Adds to the right side (end) of the deque.

        Arguments:
            value (no designated type): The value to be added to the right of the deque.
        """

        self.arr.append(value)
        self.rightValue = value
        self.length += 1

        if self.leftValue == None:
            self.leftValue = value


    def removeRightDeque(self):
        """
        Removes from the right side (end) of the deque.
        """

        self.arr.pop()
        self.length -= 1

        if len(self.arr) == 0:

            self.leftValue = None
            self.rightValue = None

        else:
            self.rightValue = self.arr[self.length]
