class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
  
    def degree(self):
        return len(self.edges)
  
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return "Vertex({})".format(repr(self.value))
