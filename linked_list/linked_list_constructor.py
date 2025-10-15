
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        #def append(value):
        #def prepend(value):
        #def insert(self,value, position):

my_linked_list = LinkedList(1)
print(my_linked_list)





def print_list(node):
    temp = node
    while temp is not None:
        print(temp.value)
        temp = temp.next    
            