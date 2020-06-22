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

# Remove From Top
def pop(self):
    value = self.head.value
    self.head = self.head.next
    return value

LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


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