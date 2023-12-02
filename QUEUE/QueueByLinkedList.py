""""Queue Using Linked List"""
class Node:
    def __init__(self,items=None,next=None):
        self.items = items
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None
    def enqueue(self,data):
        #Make a new Node
        n = Node(data)
        #case 1 where Queue is empty
        if self.is_empty():
            self.front = n
        else:#Queue not empty put the element at rear
            self.rear.next = n
        self.rear = n
        self.item_count +=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front == self.rear:#Only 1 node is present
            self.front = None
            self.rear = None
        else:#More than 1 node present change in front not at rear
            self.front = self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("No Data in the queue")
        else:
            return self.front.items
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No Data is in the queue")
        else:
            return self.rear.items
    def size(self):
        return self.item_count
#Driver Code
q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print("After Dequeue")
print(q1.get_front(),q1.get_rear())
            