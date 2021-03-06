class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

  
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
 
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
 
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
 
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
 
    def add_to_head(self, value):
        #wrap the given value in a ListNode
        new_node = ListNode(value)
        self.length += 1
         #handle if list has no head
        if self.head:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
        else: 
            self.head = new_node
            self.tail = self.head
  
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value 
    
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        # there is a tail
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        else: 
            self.tail = new_node
            self.head = new_node 
 
    def remove_from_tail(self):
        value = self.tail.value 
        
        if not self.tail: 
            return
        # if head and tail are the same (1 node)
        elif self.head == self.tail: 
            self.head = None
            self.tail = None 

        
        # if more than 1 node
        else: 
            self.tail = self.tail.prev 
            self.tail.next = None 

        self.length -= 1

        return value 
 
    def move_to_front(self, node):
        
   
        if node is self.head:
            return 
        value = node.value 
        self.delete(node)
        self.add_to_head(value)
 
    def move_to_end(self, node):
        if node is self.tail: 
            return 
        value = node.value 
        self.delete(node)
        self.add_to_tail(value)
        # pass
 
    def delete(self, node):
        # if list is empty
        if not self.head: 
            print("You got nothing on me")
            return
        # if node is head
        self.length -= 1

        if self.head == self.tail: 
            self.head = None
            self.tail = None 
        #we have at least 2 nodes, and the node we want to delete is the head
        if node == self.head: 
            self.head = node.next 
            self.head.prev = None 

         #we have at least 2 nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None 

        else: 
            # if somewhere in the middle
            node.delete()

        pass
 
    def get_max(self):
        highest_value = self.head.value
        current_node = self.head 

        while current_node is not None:
            
            if current_node.value > highest_value:
                highest_value = current_node.value
            current_node = current_node.next 
            
        return highest_value
 
       
    def find_middle(self):
        middle = self.head 
        end = self.head 

        while end != None and end.next.next != None: 
            end = end.next.next
            middle = middle.next 
             
        
        print(middle)
        return middle 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_nodes = 0

        self.dll = DoublyLinkedList()
        

    def append(self, item):
        if self.dll.length < self.capacity: 
            self.dll.add_to_tail(item)
            self.current_nodes = self.dll.tail
        else: 
            if self.current_nodes == self.dll.tail:
                self.current_nodes = self.dll.head
            else:
                self.current_nodes = self.current_nodes.next
                # need it to keep going if more than one extra is added 
            self.current_nodes.value = item
        # pass 

    def get(self):
        node = self.dll.head 
        temp_list = []
        while node is not None: 
            temp_list.append(node.value)
            node = node.next 
        return temp_list 


buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
buffer.append('f')
print(buffer.get())
# print(buffer)
# ['f', 'b', 'c', 'd', 'e'])
# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current_nodes = 0
#         self.storage = [] 
 
  
#     def append(self, item):
#         if len(self.storage) < self.capacity:
#             self.storage.append(item)
#         else: 
#             self.storage[self.current_nodes] = item 
#             if self.current_nodes < len(self.storage) - 1: 
#                 self.current_nodes += 1
#             else: 
#                 self.current_nodes = 0

#     def get(self):
#         return self.storage
         