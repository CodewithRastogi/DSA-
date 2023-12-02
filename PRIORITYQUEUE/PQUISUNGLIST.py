""""Priority Queue Using List"""
class PriorityQueue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items) == 0
    def push(self,data,priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index+=1
        self.items.insert(index,(data,priority))
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)
    def size(self):
        return len(self.items)
#Driver Code
p = PriorityQueue()
p.push("Abhishek",1)
p.push("Prafful",2)
p.push("Prashant",3)
p.push("Sunjay",4)
while not p.is_empty():
    print(p.pop())
print(p.size())