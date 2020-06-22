""" NODE Class """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

""" LINKEDLIST Class """ 
class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def printValues(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.value)
            tempNode = tempNode.next

# #----------------------------------------------------#
# def prepend(self, value):
#     """ Prepend a node to the beginning of the list """

#     if self.head is None:
#         self.head = Node(value)
#         return

#     new_head = Node(value)
#     new_head.next = self.head
#     self.head = new_head
# #----------------------------------------------------#

# Define a function outside of the class
def prepend(self, value):
    tempNode = Node(value)
    tempNode.next = self.head
    self.head = tempNode


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

# #----------------------------------------------------#
# def append(self, value):
#     """ Append a node to the end of the list """
#     # Here I'm not keeping track of the tail. It's possible to store the tail
#     # as well as the head, which makes appending like this an O(1) operation.
#     # Otherwise, it's an O(N) operation as you have to iterate through the
#     # entire list to add a new tail.

#     if self.head is None:
#         self.head = Node(value)
#         return

#     node = self.head
#     while node.next:
#         node = node.next

#     node.next = Node(value)
# #----------------------------------------------------#

# Insert Value From the End
def append(self, value):
    if self.head is None:
        self.head = Node(value)
        return
    
    tempNode = self.head
    while tempNode.next:
        tempNode = tempNode.next
    tempNode.next = Node(value)

LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# #----------------------------------------------------#
# def search(self, value):
#     """ Search the linked list for a node with the requested value and return the node. """
#     if self.head is None:
#         return None

#     node = self.head
#     while node:
#         if node.value == value:
#             return node
#         node = node.next

#     raise ValueError("Value not found in the list.")

# #----------------------------------------------------#

# Search Value From Link List
def search(self, value):
    tempNode = self.head
    while tempNode:
        if value == tempNode.value:
            return tempNode
        tempNode = tempNode.next
    
    return None

LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# #----------------------------------------------------#
# def remove(self, value):
#     """ Delete the first node with the desired data. """
#     if self.head is None:
#         return

#     if self.head.value == value:
#         self.head = self.head.next
#         return

#     node = self.head
#     while node.next:
#         if node.next.value == value:
#             node.next = node.next.next
#             return
#         node = node.next

#     raise ValueError("Value not found in the list.")

# #----------------------------------------------------#

# Remove From List
def remove(self, value):
    tempNode = self.head
    prevNode = None
    while tempNode:
        
        if tempNode.value == value:
            break;
            
        prevNode = tempNode
        tempNode = tempNode.next
    
    if tempNode is None:
        return -1
    elif tempNode is self.head:
        self.head = tempNode.next
    else:
        prevNode.next = tempNode.next
    

LinkedList.remove = remove

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

# #----------------------------------------------------#
# def pop(self):
#     """ Return the first node's value and remove it from the list. """
#     if self.head is None:
#         return None

#     node = self.head
#     self.head = self.head.next

#     return node.value
# #----------------------------------------------------#

# Remove From Top
def pop(self):
    if self.head is None:
        return None

    value = self.head.value
    self.head = self.head.next
    return value

LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

# #----------------------------------------------------#
# def insert(self, value, pos):
#     """ Insert value at pos position in the list. If pos is larger than the
#         length of the list, append to the end of the list. """
#     # If the list is empty 
#     if self.head is None:
#         self.head = Node(value)
#         return
        
#     if pos == 0:
#         self.prepend(value)
#         return

#     index = 0
#     node = self.head
#     while node.next and index <= pos:
#         if (pos - 1) == index:
#             new_node = Node(value)
#             new_node.next = node.next
#             node.next = new_node
#             return

#         index += 1
#         node = node.next
#     else:
#         self.append(value)
        
# #----------------------------------------------------#

# Insert Value by using Index
def insert(self, value, pos):
    tempNode = self.head

    if not tempNode or pos == 0:
        self.head = Node(value)
        self.head.next = tempNode
        return
    
    index = 0
    prevNode = self.head
    while tempNode.next:
        if index == pos:
            break
        prevNode = tempNode 
        tempNode = tempNode.next 
        index+=1

    if not tempNode.next:
        tempNode.next = Node(value)
    else:
        newNode = Node(value)
        prevNode.next = newNode
        newNode.next = tempNode

LinkedList.insert = insert

# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# #----------------------------------------------------#

# def size(self):
#     """ Return the size or length of the linked list. """
#     size = 0
#     node = self.head
#     while node:
#         size += 1
#         node = node.next

#     return size
# #----------------------------------------------------#

# Find Lenght of LinkList
def size(self):
    tempNode = self.head
    count = 0
    while tempNode:
        count+=1
        tempNode = tempNode.next
    
    return count

LinkedList.size = size

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

print(" All Correct!! ")