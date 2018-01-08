class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
  
    def degree(self):
        return len(self.edges)

    def getNeighbors(self):
        neighbors = []
        for edge in iter(self.edges.values()):
            neighbor = edge.w if edge.w.value != self.value else edge.v
            neighbors.append(neighbor)
        return neighbors 

  
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return "Vertex({})".format(repr(self.value))
