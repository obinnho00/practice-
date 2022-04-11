class vertex():
    
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class graph():
 
    
    def __init__(self):
        self.edge = []
        self.vertex = []
        self.graph = []
             
        
    # function to keep count of the how many item are in vertex 
    def count(self):
        global  count
        count = []
        count.append(len(self.vertex))
        print(count)
        
    def add_vertex(self, vale): 
        global count
        count = 0
        if vale in self.vertex:
            print(vale,"data in graph")
        else:
            count += 1
            self.vertex.append(vale)
            #print(count)
            
            
            for roll in self.graph:
                roll.append(0)
                
            colum = []
            for j in range(count):
                colum.append(0)
            self.graph.append(colum)
            
    
            
    def matrix(self):
        for i in range(count):
            for j in range(count):
                print("")
                
            print(self.graph[i][j],end=" ")
            
            
    def printgrph(self):
        if self.vertex:
            print(self.vertex)
        else:
            print("nothing to show!")
            
    #add the the connection between friends
    #unweighted and undirected graph 
        
    def add_edge(self,val, val2):
        
        if val not in self.vertex:
            
            print(val,"not in graph")
        elif val2 not in self.vertex:
            print(val2,"is not in graph")
        else:
            index_of_val = self.vertex.index(val) # checks for the the index conection of the two item
            index_of_val2 = self.vertex.index(val2)
            
            self.graph[index_of_val] [index_of_val2] = 1
            self.graph[index_of_val2] [index_of_val2] = 1
            
    #weighted and directed
        
    def add_direc(self, num1, num2, cost):
        if num1 not in self.graph:
            
            print("NOT IN HRAPH")
        elif num2 not in self.graph:
            print(" NOT IN GRAPH")
        else:
            v1 = self.vertex.index(num1)
            v2 = self.vertex.index(num2)
            self.graph[v1][v2] = 10
            self.graph[v2][v1] = 10
            
        
    def remove_vertex(self, roll, colum):
        if roll not in self.vertex:
            print(roll, "no vertex for that")
        if colum not in self.vertex:
            print(colum, "no vertex in graph")
        else:
            roll_index = self.vertex.index(roll)
            colum_index = self.vertex.index(colum)
            #now get the asginin the index showing the connection
            self.graph[roll_index][colum_index] = 0
            self.graph[colum_index][roll_index] = 0
        
            
            
        
        
            

            
            
        
val = graph()
val.add_vertex("A")
val.add_vertex("B")
val.add_vertex("C")
val.add_vertex("D")
val.add_vertex("E")
val.add_vertex("F")
val.add_vertex("H")
val.printgrph()
val.add_edge("A", "B")
val.add_edge("A", "B")
val.matrix()
val.count()