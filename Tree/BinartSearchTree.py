"""Insertion , Searching , Traversing and Deletion in Binary Search Tree"""
class Node:
    def __init__(self,item = None,left = None,right = None):
        self.item = item
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    #Insertion
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root
    #Searching
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.itemm == data:
            return root
        if data < root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    #Traversing
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
           
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
    #Minimum Value in Tree
    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    #Maximum Value in Tree        
    def max_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item
    #Size
    def size(self):
        return len(self.inorder())
    #Delete 
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:#1 Child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            #2 children
            #Ether represent it with predecessor(Big value from left child) or successor(Small value from right child)
            root.item = self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root
            
            
#Driver Code           
b = BST()
b.insert(10) 
b.insert(15) 
b.insert(2) 
b.insert(8) 
b.insert(5)
print(b.inorder())
print(b.postorder() )
print(b.preorder() )
print(b.min_value(b.root))
print(b.max_value(b.root))
print("Size of the Binary search tree",b.size())
b.delete(8)
print(b.inorder())
print("Size of the Binary search tree",b.size())