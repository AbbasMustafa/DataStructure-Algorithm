class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

# -------------------------------

# Creating Loop
list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

#-------------------------------
# O(n)
# def iscircular(linked_list):
#     """
#     Determine wether the Linked List is circular or not

#     Args:
#        linked_list(obj): Linked List to be checked
#     Returns:
#        bool: Return True if the linked list is circular, return False otherwise
#     """

#     if linked_list.head is None:
#         return False
    
#     slow = linked_list.head
#     fast = linked_list.head
    
#     while fast and fast.next:
#         # slow pointer moves one node
#         slow = slow.next
#         # fast pointer moves two nodes
#         fast = fast.next.next
        
#         if slow == fast:
#             return True
    
#     # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
#     # the list has an end and isn't circular
#     return False

# O(N^2)
def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    if linked_list:
        return True
    
    tempNode = linked_list.head
    fastRunner = tempNode
    slowRunner = tempNode
    
    count = 1
    while tempNode:
        
        slowRunner = tempNode.next
        tempNode = tempNode.next
        for i in range(count):
            fastRunner = fastRunner.next
        
        if slowRunner is fastRunner:
            return True
        
        i+=1
        
        
    
    return False

# Test Condition
# Test Cases

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")   # Fail
print ("Pass" if iscircular(LinkedList([1])) else "Fail")                 # Fail
print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
print ("Pass" if iscircular(LinkedList([])) else "Fail")                  # Fail
