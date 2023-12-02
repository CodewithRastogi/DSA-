"""Dequeue Using List"""
class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            self.items.pop() #By,default pop method delete from last
    def get_front(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            return self.items[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Dequeue is empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
#Driver Code
d1 =  Deque()
d1.insert_front(10)
d1.insert_front(50)
d1.insert_rear(60)
d1.insert_rear(80)
print("Front = ",d1.get_front(),"Rear = ",d1.get_rear())
d1.delete_front()
print("Front = ",d1.get_front(),"Rear = ",d1.get_rear())
d1.delete_rear()
print("Front = ",d1.get_front(),"Rear = ",d1.get_rear())
