from Vertex import Vertex

class Blossom():
    blossom_index = 0
    def __init__(self, v, w, tree):
        self.v = v
        self.w = w
        self.tree = tree
        self.path = None
        self.precompute_path()
        self.blossom_index = Blossom.blossom_index
        Blossom.blossom_index += 1
    def precompute_path(self):
        if self.path:
            return
        v_tree = self.tree.find(self.v)
        w_tree = self.tree.find(self.w)
        v_height = v_tree.height()
        w_height = w_tree.height()
        v_node = v_tree
        w_node = w_tree
        # Contains v, v', v'', ...
        v_value_path = []
        # Contains w, w', w'', ...
        w_value_path = []
        if v_height > w_height:
            for _ in range(v_height - w_height):
                v_value_path.append(v_node.value)
                v_node = v_node.parent
        elif w_height > v_height:
            for _ in range(w_height - v_height):
                w_value_path.append(w_node.value)
                w_node = w_node.parent
        while True:
            if v_node == w_node:
                break
            elif v_node.parent is None or w_node.parent is None:
                raise
            else:
                v_value_path.append(v_node.value)
                w_value_path.append(w_node.value)
                v_node = v_node.parent
                w_node = w_node.parent
        # Contains v, v'', v''', ... common ancestor ... w'', w', w
        self.path = v_value_path + [v_node.value] + w_value_path[::-1]
    def __str__(self):
        return "B{}".format(self.path)
    
    def __repr__(self):
        return "Blossom({}, {}, {})".format(self.v, self.w, self.tree)
    
    def contract_graph(self, graph):
        marked_vertex = Vertex("blossom-{}".format(self.blossom_index))
        connected = set()
        contraction = {}
        for node_value in self.path:
            node_vertex = graph.find_vertex(node_value)
            for connected_vertex in node_vertex.edges:
                connected.add(connected_vertex.value)
                contraction[connected_vertex.value] = node_vertex.value
            # Filter internal nodes
            if node_vertex.value in connected:
                connected.remove(node_vertex.value)
            graph.remove_vertex(node_vertex)
        graph.add_vertex(marked_vertex)
        for connected_value in connected:
          connected_vertex = graph.find_vertex(connected_value)
          assert(connected_vertex is not None)
          graph.add_edge(marked_vertex, connected_vertex)
        return contraction
    
    def get_path_index(self, value):
      for i in range(len(self.path)):
        if self.path[i] == value:
          return i
      return None
    def lift_path(self, path, contraction):
      incoming_edge = None
      outgoing_edge = None
      marked_value = "blossom-{}".format(self.blossom_index)
      for edge in path.edges:
        if edge.w.value == marked_value:
          incoming_edge = edge
      if  edge.v.value == marked_value:
          outgoing_edge = edge
      
      if incoming_edge and outgoing_edge:
        incoming_edge_value = contraction[incoming_edge.v.value]
        outgoing_edge_value = contraction[outgoing_edge.w.value]
        incoming_edge_index = self.get_path_index(incoming_edge_value)
        outgoing_edge_index = self.get_path_index(outgoing_edge_value)
        if outgoing_edge_index < incoming_edge_index:
          outgoing_edge_index += len(self.path)
        # If there are an even number of vertices between the
        # outgoing path and the incoming path, the path must be
        # reversed.
        if (outgoing_edge_index - incoming_edge_index) % 2 == 0:
          increment = -1
        else:
          increment = 1
      elif incoming_edge:
        incoming_edge_value = contraction[incoming_edge.v.value]
        incoming_edge_index = self.get_path_index(incoming_edge_value)
        outgoing_edge_index = incoming_edge_value - 1 + len(self.path)
        increment = 1
      elif outgoing_edge:
        outgoing_edge_value = contraction[outgoing_edge.w.value]
        outgoing_edge_index = self.get_path_index(outgoing_edge_value)
        incoming_edge_index = outgoing_edge_value - 1
        increment = -1
      else:
        raise
      
      index = incoming_edge_index
      end = outgoing_edge_index
      if incoming_edge:
        previous_value = incoming_edge.v.value
      else:
        previous_value = None
      while index != end:
        if previous_value:
          path.edges.append(Edge(Vertex(previous_value), Vertex(path[index])))
        previous_value = path[index]
        index += increment
      if outgoing_edge:
        path.edges.append(Edge(Vertex(previous_value), Vertex(outgoing_edge.w.value)))
      path.edges = filter(lambda edge: (marked_value not in (edge.v.value, edge.w.value)), path.edges)
