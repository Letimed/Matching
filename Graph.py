from Edge import Edge
from Vertex import Vertex

class Graph:

  def __init__(self):
    self.vertices = []
    self.edges = []

  def find_vertex(self, value):
    for vertex in self.vertices:
      if vertex.value == value:
        return vertex
    return None

  def find_edge(self, v, w):
    if w in v.edges:
      return v.edges[w]
    else:
      return None

  def add_edge(self, v, w):
    edge = self.find_edge(v, w)
    if not edge:
      edge = Edge(v, w)
      v.edges[w] = edge
      w.edges[v] = edge
      self.edges.append(edge)

  def remove_edge(self, v, w):
    edge = self.find_edge(v, w)
    if edge:
      del v.edges[w]
      del w.edges[v]
      self.edges.remove(edge)

  def add_vertex(self, vertex):
    self.vertices.append(vertex)

  def remove_vertex(self, vertex):
    for w in vertex.edges:
      edge = vertex.edges[w]
      self.edges.remove(edge)
      del w.edges[vertex]
    vertex.edges = []
    self.vertices.remove(vertex)

  def clone(self):
    g = Graph()
    for vertex in self.vertices:
      g.add_vertex(Vertex(vertex.value))
    for edge in self.edges:
      g.add_edge(g.find_vertex(edge.v.value), g.find_vertex(edge.w.value))
    return g

  def __str__(self):
    return '\n'.join([str(x) for x in \
      ["Graph{"] + self.vertices + self.edges + ["}"]])
