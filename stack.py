
class stack:
    """
    Represents a stack data structure.

    Attributes:
        arr (list): The array containing all the values in the stack.

        counter (int): Represents the current index of the last, or top, value in the stack.

        topValue (no designated type): The value at the very end of the "arr" attribute, the topmost value in the stack.

    Methods:
        __init__(self, arr)

        addStack(self, value)

        removeStack(self)

        __iter__(self)

        __next__(self)

    Notes:
        This object is both iterable and its own iterator, as it contains both the "__iter__" and "__next__" methods and its "__iter__" method returns "self."
    """

    def __init__(self, arr=[]):
        """
        Creates the instance attributes the object needs to function properly.

        Arguments:
            arr (list, optional): The list of values to be stored in the stack, left empty by default.
        """

        self.arr = arr
        self.counter = len(arr) - 1

        if len(arr) > 0:
            self.topValue = arr[-1]
        
        else:
            self.topValue = None


    def addStack(self, value):
        """
        Adds a value to the top of the stack.

        Arguments:
            value (no designated type): the value to be added to the stack.
        """

        self.counter += 1
        self.arr.append(value)

        self.topValue = self.arr[self.counter]


    def removeStack(self):
        """
        Removes the topmost value from the stack.

        Notes:
            As this is a stack data structure, removing the topmost value from the stack is both permanent and the only way to access the values stored in the rest of the stack.

            Used in the class's "__next__" method.
        """

        self.counter -= 1
        self.topValue = self.arr[self.counter]

        self.arr.pop()


    def __iter__(self):
        """
        Simply returns "self," as the object is its own iterator.

        Returns:
            self (stack): The object given to the "__next__" method is the instance itself, as this object is its own iterator.
        """

        return self

    
    def __next__(self):
        """
        Used to iterate over the contents of the stack. Returns and remembers one value at a time until the end of the stack is reached.

        Returns:
            current (no desgnated type): The topmost value of the array within the stack.

        Notes:
            Due to the nature of stack data structures, iterating over the stack from top to bottom also erases the contents of the stack, as the topmost value must be deleted
            before further values can be analyzed. Be warned that you can only iterate over a stack once because of this.
        """
        if self.counter <= -1:
            raise StopIteration
        
        current = self.topValue
        self.removeStack()

        return current
