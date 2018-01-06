from Graph import Graph
from Vertex import Vertex

class Matching(Graph):
  
    def augment_along(self, path):
        for edge in path.edges:
            v_vertex = self.find_vertex(edge.v.value)
            w_vertex = self.find_vertex(edge.w.value)
            assert(v_vertex is not None and w_vertex is not None)
            vw_edge = self.find_edge(v_vertex, w_vertex)
            if vw_edge:
                self.remove_edge(v_vertex, w_vertex)
            else:
                self.add_edge(v_vertex, w_vertex)
    
    def get_matched(self, value):
        vertex = self.find_vertex(value)
        assert(vertex is not None)
        assert(len(vertex.edges) == 1)
        for vertex in vertex.edges:
            return vertex
    
    @staticmethod
    def from_graph(source):
        m = Matching()
        for vertex in source.vertices:
            m.add_vertex(Vertex(vertex.value))
        return m