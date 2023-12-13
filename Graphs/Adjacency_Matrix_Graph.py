"""Undirected Graph"""
class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_matrix = [[0] * vno for e in range(vno)]
    #Add-Edge
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")
    #Remove-Edge
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")
    #Node exists or not
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v]!=0
        else:
            print("Invalid vertex")
    #Print Graph
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))
#Driver Code
g = Graph(4)
g.add_edge(0,1)           
g.add_edge(2,1)           
g.add_edge(0,3)           
g.add_edge(0,2)           
g.add_edge(3,1)           
g.add_edge(1,1)
g.remove_edge(1,1)
print("Has Node Exists ",g.has_edge(0,1))
print("Has Node Exists ",g.has_edge(1,1))
g.print_adj_matrix()           
            