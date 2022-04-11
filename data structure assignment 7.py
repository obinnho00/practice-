class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prv = None
        
class linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addNode(self, new_node):
        new_node = Node(new_node)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def remove_dup(self, val):
        if self.head == None:
            return self.head
        cur = self.head
        prv = None
        while cur != None:
            if cur.data == val:
                if prv == None:
                    cur = cur.next
                else:
                    prv.next = cur.next
            else:
                prv = cur 
            cur = cur.next 
        return self.head
        
     
    def printlist(self):
        
        while self.head:
            print(self.head.data)
            self.head = self.head.next
        else:
            print("tail points to --> null!")
        
    
        
        
val = linklist()
val.addNode(2)
val.addNode(3)
val.addNode(4)
val.addNode(5)
val.addNode(3)
val.printlist()

""" 
class vertex:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class adjacencyList:
    
   def __init__(self):
       self.vertex = {}
       
       
   def add_vertex(self,data):
       if data in self.vertex:
           print(data,"already existed")
       else:
           self.vertex[data] = []
             
           
   def add_edge(self, v1,v2):
       if v1 not in self.vertex:
           print(v1,"not in graph")
       elif v2 not in self.vertex:
           print(v2,"not in graph")
       else:
           self.vertex[v1].append(v2 ) 
           self.vertex[v2].append(v1 )
           
   
   def printlist(self):
       if self.vertex:
           print(self.vertex)
       else:
           print(self.vertex,"not value sorry!")
   
      
val = adjacencyList()
# ADD VERTEX
val.add_vertex("A")
val.add_vertex("B")
val.add_vertex("C")
#val.add_edge("B","C")
val.add_vertex("D")
val.add_vertex("E")
val.add_vertex("F")

# CONNECT THE VERTEX

val.add_edge("A","B")
val.add_edge("B","E")
val.add_edge("A","C")
val.add_edge("A","D")
val.add_edge("C","D")
val.add_edge("B","D")
val.add_edge("D","E")
val.add_edge("E","F")
#val.add_edge("A","B")
#val.add_edge("A","B")
#val.add_edge("A","B")

val.printlist()





"""












