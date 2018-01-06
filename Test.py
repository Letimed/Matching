class Tests:
    def simple(self):
        """
        A simple test

        >>> g = Graph()
        >>> g.add_vertex(Vertex(2))
        >>> g.add_vertex(Vertex(1))
        >>> g.add_vertex(Vertex(0))
        >>> g.add_vertex(Vertex(3))
        >>> g.add_edge(g.find_vertex(1), g.find_vertex(2))
        >>> g.add_edge(g.find_vertex(0), g.find_vertex(3))
        >>> g.add_edge(g.find_vertex(2), g.find_vertex(3))
        >>> m = Matching.from_graph(g)
        >>> m = find_maximum_matching(g, m)
        >>> print m
        Graph {
        2
        1
        0
        3
        <0, 3>
        <1, 2>
        }
        """
        pass
    def loop(self):
        """
        A test containing a loop
        
        >>> g = Graph()
        >>> g.add_vertex(Vertex(1))
        >>> g.add_vertex(Vertex(2))
        >>> g.add_vertex(Vertex(3))
        >>> g.add_vertex(Vertex(4))
        >>> g.add_vertex(Vertex(5))
        >>> g.add_vertex(Vertex(6))
        >>> g.add_edge(g.find_vertex(1), g.find_vertex(2))
        >>> g.add_edge(g.find_vertex(2), g.find_vertex(3))
        >>> g.add_edge(g.find_vertex(3), g.find_vertex(4))
        >>> g.add_edge(g.find_vertex(4), g.find_vertex(5))
        >>> g.add_edge(g.find_vertex(5), g.find_vertex(6))
        >>> g.add_edge(g.find_vertex(6), g.find_vertex(2))
        >>> m = Matching.from_graph(g)
        >>> m = find_maximum_matching(g, m)
        >>> print m
        Graph {
        1
        2
        3
        4
        5
        6
        <5, 6>
        <3, 4>
        <1, 2>
        }
        """
        pass