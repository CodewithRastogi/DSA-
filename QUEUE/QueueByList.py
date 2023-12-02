""""Queue Using List"""
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)#Pop element at index 0
        else:
            raise IndexError("Queue Underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1] # Return last index element from the queue.
        else:
            raise IndexError("Queue Underflow")
    def size(self):
        return len(self.items)
    
#Driver Code
q1 = Queue()
#Handling If no element is in the queue.
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())

q1.dequeue()
print("Front = ",q1.get_front(),"Rear = ",q1.get_rear())

#Handling, Deletion case.
try:
    q1.dequeue()
    print("Queue has now ",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])
