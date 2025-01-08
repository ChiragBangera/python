# Create a node

class Node:
    def __init__(self, value):
        self.value =  value
        self.next =  None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        # printing the linked list
        temp_node = self.head
        res = ''
        
        while temp_node:
            res += str(temp_node.value)
            
            if temp_node.next:
                res += ' -> '
            
            temp_node = temp_node.next
            
        return res
        
    def append(self, value):
        new_node = Node(value)
        
        # if the Linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # when the linked list already has values in them
        # change tails next reference to the new node
        # and change the tail node to the new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length +=1
        
    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        
        if index < 0 or index > self.length:
            return False
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        
        else:
            for _ in range(index - 1):
                # itirate till the index - 1 where you want to insert the value
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def search(self,  target):
        current = self.head
        while current:
            if current.value == target:
                print(f"{target} in linked list")
                return current.value
            current = current.next
        print(f"{target} not in linked list")
            
    def get(self, index):
        
        if index < 0 or index >= self.length:
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current
            
    def set_value(self, index, value):
        
        target = self.get(index)
        if target:
            target.value = value
            return True
        return False
            
    def pop_first(self):
        current = self.head
        
        if self.length == 0:
             return None
        
        if self.length == 1:
            self.head == None
            self.tail == None
            return current
        
        self.head = current.next
        current.next = None
        self.length -= 1
        return current
    
    def pop(self):
        
        if self.length == 0:
             return None
        
        if self.length == 1:
            self.head == None
            self.tail == None
            return current
        
        current = self.get(self.length - 2)
        self.tail = current
        current.next = None
        self.length -=1
        
    def remove(self, index):
        
        if index < -1 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1 or index == -1:
            return self.pop()
        
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
linkedlist_instance = LinkedList()
linkedlist_instance.append(10)
linkedlist_instance.append(20)
linkedlist_instance.append(30)
linkedlist_instance.append(40)
linkedlist_instance.prepend(50)
linkedlist_instance.insert(2, 200)
linkedlist_instance.insert(0, 100)
linkedlist_instance.search(34)
linkedlist_instance.search(30)
linkedlist_instance.search(50)
print(linkedlist_instance.get(4))
print(linkedlist_instance.get(49))
print(linkedlist_instance.get(6))
print(linkedlist_instance.set_value(6, 45))
print(linkedlist_instance)
linkedlist_instance.pop_first()
linkedlist_instance.pop()
linkedlist_instance.remove(3)
linkedlist_instance.remove(-1)
linkedlist_instance.delete_all()
print(linkedlist_instance)