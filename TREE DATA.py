class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # A) insert a Node
class Tree:
    def __init__(self, root):
        self.root = root
    
    
    def insert(self, data):
        if self.root is None:
            self.root = data
        else:
            if data < self.root:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.root:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            
                    
                    
                    #B) inserct a node
                    
    def preorder_print(self, tree):
        """print-->root,left--->right """
        if tree:
            if tree.left:
                self.preorder_print(self.root)
                self.preorder_print(root.left)
                self.preorder_print(root.right)
                print(tree.root)
        else:
            return
        
        
    def inorder(self, tree):  # "left root right"
        if tree is None:
            print('tree is empty')
        else:
            if tree.left:
                self.inorder(tree.left)

            print(tree.root)
                
            if tree.right:
                self.inorder(tree.right)
                
    def search(self, item):
        if self.root is None:
            return
        if self.root == item:
            return self.root
            print("found")
        if self.root > item:
            if self.left:
                return self.search(root.left)
            else:
                print("tree has no left childern ")
                
        if self.root < item:
            if self.right:
                return self.search(root.right)
            else:
                print("item not found on terminal")
            
            
            
        
         
                  
                    
            
                
                
        
                
                
    
            
    
                


root = Tree(3)
root.insert(0)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)
#root.delect_node(5)
#root.preorder_print(root)
root.inorder(root)  
root.search(67)
#print("root = ", root.root)          