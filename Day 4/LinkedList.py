class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
            
    def insert(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def printValues(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.value)
            tempNode = tempNode.next
        
    def to_list(self):
        out_list = []

        tempNode = self.head
        while tempNode:
            out_list.append(tempNode.value)
            tempNode = tempNode.next

        return out_list


def create_linked_list(input_list):
    if(input_list == []):
        return None
    ll = LinkedList()
    for i in range(len(input_list)):
        ll.insert(input_list[i])
    
    head = ll
    return head


linklist = create_linked_list([1,2,3,4,5])
linklist.printValues()
print(linklist.to_list())

