"""1. Best Time to Buy and Sell Stock (LeetCode 121) 
You are given a list prices where prices[i] is the price of a given stock on the ith day. You 
want to maximize your profit by choose a single day to by one stock and choosing a 
different day in the future to sell that stock. 
Your program should display which day to buy and which day to sell stock and your 
profit. 
 
Use the following lists of prices to test your program: 
• Prices = [7, 1, 5, 3, 6, 4] 
o Your program should be able to display buy the stock on day 2 and sell the 
stock on day 5, and the profit is 5 
• Prices = [7, 6, 4, 3, 1] 
o Your program should be able to display not buying the stock and the profit 
is 0 """

def stock_track():
    price = [7, 6, 4, 3, 1]
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(price):
        if price[buy] < price[sell]:
            profit = price[sell] - price[buy]
            max_profit = max(max_profit, profit)

        else:

            buy = sell
        sell += 1
    print(max_profit)


stock_track()
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
        x 
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self,data,cur_node):
        
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)   
        
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
                    
        else:
            print("BST do not support duplicate number. the",data," number already in tree!")
            
                       
    def inorder(self):
        if self.root:
           print("inoder left-->right-->root")  
           self._inorder(self.root) 
           
    def _inorder(self,cur_node):   
        if cur_node:
            self._inorder(cur_node.left)
            print(cur_node.data,end=" ")
            self._inorder(cur_node.right)
                  
    
    def post_order(self): 
        if self.root:
            print("post oredr right-->left-->root")
            self._post_order(self.root)
        else:
            print("No item in Tree")
            
    def _post_order(self,data, cur_node):
        if cur_node:
            self._post_order(data, cur_node.left)
            print(cur_node.root)
            self._post_order(data,cur_node.right)
        else:
            return 
        
    def _pre_order(self,cur_node):
        if cur_node:
            self._pre_order(cur_node.root)
            if cur_node.left:
                self._pre_order(cur_node.left)
                print(cur_node.left)
            else:
                return
            if cur_node.right:
                self._post_order(cur_node.right)
                print(cur_node.right)
            else:
                return
            
            
                
            print(cur_node.data)
            self._pre_order(cur_node.right)

        else:
            return
        
    def pre_order(self):
        if self.root:
            print("pre order root-->left-->right")
            self._pre_order(self.root)
        else:
            print("no item in list")
        
    def removeNode(self, value):
        if self.root:
            self._remove(self.root, value)
        else:
            return
    def _remove(self, value, cur_node):
        if cur_node:
            for value in len(cur_node.value):
                if value < cur_node.value:
                    self._remove(cur_node.left)
                    if value:
                        if value.left:
                            leef = value.left
                            value.left = value
                            value = leef
                            self._remove(leef)
                        elif value.right:
                            leef = value.right
                            value.right = value
                            value = leef
                            self._remove(leef)
                        else:
                            self._remove(value)
                    else:
                        print("item not i tree")
                        
                elif value > cur_node.value:
                    self._remove(cur_node.right)
                    if value:
                        if value.left:
                            leef = value.left
                            value.left = value
                            value = leef
                            self._remove(leef)
                        elif value.right:
                            leef = value.right
                            value.right = value
                            value = leef
                            self._remove(leef)
                        else:
                            self._remove(value)
                    else:
                        print("item not i tree")
        else:
            print("you dont have item in tree")
            
    def serch_item(self,data):
        if self.root:
            self._search(self.root,data)
        else:
            print("item root")
            
    def _search(self, data, cur_node):
        if cur_node:
            for i in range(len(cur_node.data)):
                if data < cur_node.data:
                    self._search(cur_node.left)
                    if data:
                        return True
                    else:
                        return False
                elif data > cur_node.data:
                    self._search(cur_node.right)
                    if data:
                        return True
                    else:
                        return False
        else:
            return "no item"
                
            
            
            
             
val = BST()
val.insert(1)
val.insert(2)
val.insert(23)
val.insert(22)
val.insert(27)
val.insert(25)
val.insert(15)
val.insert(50)
val.insert(95)
val.insert(60)
val.insert(40)
val.insert(29)



#val.inorder()
#val.pre_order()
#val.post_order()
#val.removeNode(4)
#val.serch_item(6)


























































print("\nQueation 2. Reverse linked list (LeetCode 206)\n")


'''2. Reverse linked list (LeetCode 206) 
Given the head of a singly linked list, reverse the list without creating a new list.  
 
Use the following numbers to test your program:  
[12, 4, 56, 89, 33, 15] 
Your program should be able to display the linked list from head as: 15, 33, 9, 56, 4, 12'''
 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linklist:
    def __init__(self):
       self.head = None
       self.tail = None
       self.cur = None
      
       
    def append(self, data): 
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
                
    def reverse(self):
       self.prv = None
       while self.head:
           self.cur = self.head
           self.head = self.head.next
           self.cur.next = self.prv
           self.prv = self.cur
       return self.prv
       
    def orignal(self):
       while self.head:
           print(self.head.data)
           self.head = self.head.next
    
    def printrevers(self):
        while self.prv:
            print(self.prv.data)
            self.prv = self.prv.next
   
num = linklist()
num.append(12)
num.append(4)
num.append(56)
num.append(89)
num.append(33)
num.append(15)
num.reverse()
num.orignal()
num.printrevers()
































































































