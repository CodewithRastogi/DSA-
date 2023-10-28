class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item =  item
        self.prev = prev
        self.next = next

class CDLL:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():# 0 node is present
            n.next = n
            n.prev = n
        else: #More than 1 node present
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n
    def search(self,data):
        temp = self.start
        if temp == None:
            return None
        if temp.item == data:#Check only for the 1 Node
            return temp
        else:
            temp = temp.next
        while temp != self.start:#Check when more tha 1 Node present
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item,end=' ')
            temp = temp.next
            while temp != self.start:
                print(temp.item,end=' ')
                temp = temp.next
         
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:#only, 1 Node is present
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
    def delete_last(self):
        if self.start is not None:
            if self.start.next  == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev  = self.start.prev.prev
    def delete_item(self,data):
        if self.start is not None:
            temp = self.start
            if temp.item == data: #Check for the first node
                self.delete_first()
            else:
                temp = temp.next
                while temp is not self.start:
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                    temp = temp.next
        else:
            print("List is Empty")
    def __iter__(self):
        return CDLLIterator(self.start)


class CDLLIterator:
    def __init__(self,start):
        self.current = start
        self.count = 0
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        #When to stop
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data  

#Driver Code
mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),25)
mylist.insert_at_start(100)
mylist.print_list()
print()
mylist.delete_first()
for x in mylist:
    print(x,end=' ')
print()
mylist.delete_last()
for x in mylist:
   print(x,end=' ')
print()
mylist.delete_item(25)
for x in mylist:
    print(x,end=' ')
print()

                    