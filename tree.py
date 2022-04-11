class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        
        
        
class linklists:
    def __init__(self,data):
        self.head = None
        self.current = None
        self.tail = None
        
        
    def additem(self, new_node):
        if self.current == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node.next
            self.tail = new_node
            
            
    def addafter(self, item, data):
        n = self.head 
        while n is not None:
            if n == n.data:
                break
            n = n.next
        if n is None:
            print("item is not in the list")
        else:
            new_node = Node(item)
            new_node.next = n.next
            n.next = new_node
            
    def print(self):
        while self.head != None:
            print(self.head.data)
        else:
            if self.head == None:
                print("no node")
                return
            
            
            
         
    
        
        
val = linklists      
val.additem(32)          
#val.additem(21)    
#val.additem(55)  
val.print ()     
        
        
     
            
        