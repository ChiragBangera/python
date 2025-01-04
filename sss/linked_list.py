class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # updating the previous tail pointer reference to the new_node
            self.tail.next = new_node
            # updating the tail node itself
            self.tail = new_node
        self.length += 1
        
    def __str__(self):
        temp_node = self.head
        res = ''
        while temp_node is not None:
            res += str(temp_node.value)
            if temp_node.next is not None:
                res += ' -> '
            temp_node = temp_node.next
        return res
    
    
    

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)