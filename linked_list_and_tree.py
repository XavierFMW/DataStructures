
# Linked Lists

class Node():
    """ 
    Holds a value and references to 2 other objects. Specifically created for linked lists.

    Attributes:
        value (no designated type): Can hold any date type, is the data held by the node.

        next (Node): A reference to another 'Node' object, designed for the next entry in a linked list. Can be set to a None object of no such object exists.

        back (Node): Identical to the 'next' argument, but used to designate the previous object in a linked list.
    """

    def __init__(self, value, next=None, back=None):

        self.value = value

        self.next = next
        self.back = back


class linkedList():
    """
    Represents a linked list data structure.

    Attributes:
        head (Node): The first node in the linked list.

        rear (Node): The last node in the linked list.

    Methods:
        __init__(self, valueList)

        addNode(self, value)

        removeNode(self, value)

        removeAllNodes(self, value)

        countNodes(node)
    """

    def __init__(self, valueList):
        """
        Creates relationships between 'Node' objects to form a linked list, designates instance specific 'head' and 'rear' nodes. 

        Arguments:
            valueList (list): A list of any number and type of values which will be converted into a linked list, order will be preserved.
        """

        nodeList = []

        for item in valueList:

            if isinstance(item, Node):
                nodeList.append(item)
            else:
                nodeList.append(Node(item))

        for index, node in enumerate(nodeList):

            if node != nodeList[-1]:
                node.next = nodeList[index + 1]

            if index != 0:
                node.back = nodeList[index - 1]

        
        self.head = nodeList[0]
        self.rear = nodeList[-1]

    
    def addNode(self, value):
        """
        Adds a value to the end of a linked list.

        Arguments:
            self (linkedList): As this is a class method, a specified linked list is required.

            value (no designated type): The value to be added to the end of the linked list.
        """
        self.rear.next = Node(value)
        self.rear = self.rear.next

    
    def removeNode(self, value):
        """
        Removes the first node in a linked list of a designated value.

        Arguments:
            self (linkedList): As this is a class method, a specified linked list is required.

            value (no designated type): The value to be removed from the linked list.

        Notes:
            This method uses so many conditional statements because of the relationships which must be preserved in a linked list. There's
            almost certainly a better way to write this, but I don't know what it is.
        """
        
        node = self.head

        while node != None:
            
            if node.value == value:

                if node.next != None and node.back != None:
                    node.back.next = node.next
                    node.next.back = node.back
                
                elif node.next == None:
                    node.back.next = None

                elif node.back == None:
                    node.next.back = None

                
                if node == self.head:
                    self.head = node.next
                
                elif node == self.rear:
                    self.rear = node.back


                del node

                break

            node = node.next


    def removeAllNodes(self, value):
        """
        Removes all nodes of a designated value from a given linked list.

        Arguments:
            self (linkedList): As this is a class method, a specified linked list is required.

            value (no designated type): The value to be removed from the linked list.

        Notes:
            As stated in the 'removeNode' method's docstring, there's almost certainly a better way to remove nodes from a linked list while correcting the 
            relationships between nodes, but I don't know what that is. Yes, I am very lazy.

        """
        
        node = self.head

        while node != None:
            
            del_node = node
            node = node.next

            if del_node.value == value:

                if del_node.next != None and del_node.back != None:
                    del_node.back.next = del_node.next
                    del_node.next.back = del_node.back
                
                elif del_node.next == None:
                    del_node.back.next = None

                elif del_node.back == None:
                    del_node.next.back = None

                
                if del_node == self.head:
                    self.head = del_node.next
                
                elif del_node == self.rear:
                    self.rear = del_node.back


                del del_node


@staticmethod
def countNodes(node):
    """
    Returns the number of nodes starting from a specified node to the end of that specific linked list. Does not required a linked list object, can be used on specifc sections
    of a linked list if desired.

    Arguments:
        node (Node): The node the function will begin counting from. Is included in the number of nodes counted.

    Returns:
        int: The number of nodes counted.
    """

    count = 0

    while node != None:

        count += 1
        node = node.next

    return count 



# Binary Trees 

class binaryNode():
    """
    Very similar to a 'Node' object, but specifically created for binary trees. Holds a value and references to 2 other objects.

    Attributes:
        value (no designated type): Can hold any date type, is the data held by the node.

        left (binaryNode): A refernce to another 'binaryNode' object, can be set to a None object if there is no such node to refer to.

        right (binaryNode): Identical to the 'left' argument, with the exception that it refers to a seperate node than 'left.'
        
    Notes:
        As stated in the description, this class is nearly identical to the 'Node' object used for linked lists, with the exception that it's used for binary trees
        instead.
    """

    def __init__(self, value, left=None, right=None):

        self.value = value

        self.left = left
        self.right = right


class binaryTree():
    """
    Represents a binary tree data strcuture.

    Attributes:
        root (binaryNode): The root node of the binary tree.
    """


    def __init__(self, treeArr, index=0):
        """
        Creates the relationships between 'binaryNode' objects used to form a binary tree. Similar to the 'linkedList' class, but with greater complexity.
        Represents a binary tree data strcuture.

        RECURSIVE

        Attributes:
            treeArr (list): A list of values specifically formatted for the creation of a binary tree. Check the 'Notes' section of this docstring for details.

            index (int): The index in the 'treeArr' list currently being anaylzed by the initalizer for the purpose of converting the stored data into a 'binaryNode'
                object. The funtion will act as though the index being analyzed will become the root node if set to 0.

        Notes:
            The required formatting of the 'treeArr' argument mentioned above is specifically used to store binary tree data as a list. This formatting can be seen below:

            [None, root, left, right, left.left, left.right, right.left, right.right]
              0     1      2     3        4          5           6            7

            This is a short example of the required format. Due to the way the list is formatted, the 0th index is occupied by a None object.

            The value of the root node sits at index 1. From there, every node's left node is equal to its index multiplied by 2, while its right node is equal to its index
            multiplied by 2 plus 1.

            left, i * 2
            right, i * 2 + 1

            This concept explained in greater detail can be found in this video: https://www.youtube.com/watch?v=4nJZhcD0wRA&ab_channel=CppNuts

            THIS VIDEO IS NOT MINE, show the creator some support.
        """

        if index == 0:

            self.root = binaryNode(treeArr[1])

            self.root.left = self.__init__(treeArr, 2)
            self.root.right = self.__init__(treeArr, 3)

        else:

            try:

                if treeArr[index] == None:
                    return None

                current_node = binaryNode(treeArr[index])

                current_node.left = self.__init__(treeArr, index * 2)
                current_node.right = self.__init__(treeArr, index * 2 + 1)

                return current_node

            except IndexError:
                return None


def treeSum(node):
    """
    Takes the sum of a section of a binary tree containing only floats and integers.

    RECURSIVE

    Arguments:
        node (binaryNode): The root head of the branch to be counted. The sum of this node and all subsequent nodes will be taken.

    Returns:
        float: The sum of every node on the given section of the tree.

    Raises:
        Exception: A custom exception is raised if any of the nodes of the given section of the tree cotain anything other than a 
            float or integer.
    """

    if not isinstance(node, binaryNode):
        raise Exception("The node given to the 'treeSum' function must be a binaryNode object.")

    if node == None:
        return 0

    elif isinstance(node.value, int) or isinstance(node.value, float):
            
        count = float(node.value) + treeSum(node.left) + treeSum(node.right)
        
        return count

    else:
        raise Exception("The value of all nodes in a binary tree given to the 'treeSum' function must be either integers or floats.")


def addBinaryNode(parent, direction, value):
    """
    Adds or replaces a binary node on a binary tree.

    Arguments:
        parent (binaryNode): The node of a binary tree that will have one of its child nodes replaced.

        direction (str): Either 'left' or 'right,' determines which of the parent's nodes is replaced. 

        value (no designated type): Can be of any data type. Whatever data is added will be held in a 'binaryNode' object and 
            replaces the given parent node's left or right child node. This is with the exception that the given value is either a
            'Node' or 'binaryNode' object, in which case the value of the object will be copied over to form a new object, rather 
            than the object itself.

    Raises:
        Exception: A custom exception is rasied if the 'direction' argument given isn't a string containing the words 'left' or 'right.'

    Notes:
        This function is written for the purpose of adding leaf nodes to trees, in which case the node being replaced by this function
        would simply be the value 'None' rather than a node object. Keep in mind that this function can overwrite a parent node's 
        children, and will not maintain further relationships in such cases. This does, however, add the extra functionality of 
        easily removing entire branches from a tree if a specific node is replaced.
    """

    direction = direction.lower()

    if direction != "left" and direction != "right":
        raise Exception("The direction given to the 'addBinaryNode' function must be either 'left' or 'right.' ")

    elif isinstance(value, Node) or isinstance(value, binaryNode):

        if direction == "left":
            parent.left = binaryNode(value.value)
        else:
            parent.right = binaryNode(value.value)

    else:

        if direction == "left":
            parent.left = binaryNode(value)
        else:
            parent.right = binaryNode(value)


def convertToLinkedList(arr):
    """
    Converts a list of 'binaryNode' objects into a linked list.

    Arguments:
        arr (list): The array of 'binaryNode' objects to be converted into a linkedList object. Order is preserved.

    Returns:
        linkedList: The newly converted linked list.
    """

    arrValues = []

    for node in arr:
        arrValues.append(node.value)

    return linkedList(treeValues)


def convertToTree(arr, direction='left'):
    """
    Converts a list of values into the format referenced in the 'binaryTree' docstring, then creates a binary tree using it.

    Arguments:
        arr (list): The list of values to be formatted.

        direction (str, optional): Specifices whether the produced tree will be formatted with each value being created in a chain of left or right nodes. Explained in greater
            detail in the 'Notes' section below.

    Returns:
        binaryTree: The binary tree produced using the newly formatted list.

    Raises:
        Exception: A custom exception is rasied if the 'direction' argument given isn't a string containing the words 'left' or 'right.'

    Notes:
        Based on the 'direction' string given, each value will automatically become the value before its either left or right child node. Note that this is 
        the only way trees created using this function will be formatted, and that trees formatted with more complexity must be created by hand. Sorry.
    """

    direction = direction.lower()

    if direction != "left" and direction != "right":
        raise Exception("The direction given to the 'convertToTree' function must be either 'left' or 'right.' ")
    
    index = 1
    treeList = [None, ]
    treeDict = {}

    for value in arr:

        treeDict[index] = value

        if direction == "left":
            index = index * 2

        elif direction == "right":
            index = index * 2 + 1

    for num in range(1, (list(treeDict)[-1] + 1)):

        try:
           treeList.append(treeDict[num]) 
        except KeyError:
            treeList.append(None)

    return binaryTree(treeList)
