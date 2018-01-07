from Blossom import Blossom
from Edge import Edge
from Graph import Graph

class Algo:
    def find_maximum_matching(self, graph, matching):
        path = self.find_augmenting_path(graph, matching)
        if path and len(path.edges) > 0:
            matching.augment_along(path)
            return self.find_maximum_matching(graph, matching)
        else:
            return matching
    
    def find_unmarked_vertex_with_even_distance(self, forest, marked):
        """
        Returns a value from forest that is not marked and has even height
        """
        found = None
        for tree in forest:
            for subnode in tree.subnodes():
                if marked.has_value(subnode.value) or subnode.height () % 2 != 0:
                    continue
                else:
                    found = subnode
                    break
        return found
    
    def find_unmarked_edge_incident_on_v(self, v, marked):
        """
        Returns an unmarked Edge connecting 2 values, one of which is v.
        """
        for w, edge in v.edges.items():
            if marked.has_pair(v.value, w.value):
                continue
            return edge
        return None
    
    def find_tree_in_forest(self, forest, value):
        for tree in forest:
            t = tree.find(value)
            if t:
                return t
        return None
    
    def find_augmenting_path(self, graph, matching):
        # Trees containing values that were originally in `matching`
        forest = []
    
        # Values of "marked" nodes, and Edges joining 2 values of "marked" nodes
        marked = Marked()
    
        # Mark all edges that are already in `matching`
        for edge in matching.edges:
            marked.append_pair(edge.v.value, edge.w.value)
    
        # Create a singleton tree { v } for each exposed vertex `v` in `matching`
        for vertex in matching.vertices:
            assert(vertex.degree() < 2)
            if vertex.degree() == 0:
                forest.append(Tree(vertex.value, [], None))
    
        while True:
            v_tree = self.find_unmarked_vertex_with_even_distance(forest, marked)
            if not v_tree:
                break
    
            v_value = v_tree.value
            v_vertex = graph.find_vertex(v_value)
            while True:
                e = self.find_unmarked_edge_incident_on_v(v_vertex, marked)
                if not e:
                    break
    
                # Bind `w` as the other end of edge `e`
                w_vertex = e.other(v_vertex)
                w_value = w_vertex.value
    
                # Find w_value in `forest`
                w_tree = self.find_tree_in_forest(forest, w_value)
    
                if w_tree is None:
                    # We know that w must be matched, so add vw and wx to forest
                    # where x is w's matching
                    x_value = matching.get_matched(w_value).value
                    w_tree = v_tree.add_child(w_value)
                    x_tree = w_tree.add_child(x_value)
                else:
                    if w_tree.height() % 2 == 1:
                        # Do nothing
                        pass
                    else:
                        v_root = v_tree.root()
                        w_root = w_tree.root()
                        if v_root != w_root:
                            p = Path()
                            node = v_tree
                            while node.parent:
                                p.edges.append(graph.find_edge(
                                    graph.find_vertex(node.value),
                                    graph.find_vertex(node.parent.value)))
                                node = node.parent
                            p.edges = p.edges[::-1]
                            p.edges.append(e)
                            node = w_tree
                            while node.parent:
                                p.edges.append(graph.find_edge(
                                    graph.find_vertex(node.value),
                                    graph.find_vertex(node.parent.value)))
                                node = node.parent
                            return p
                        else:
                            blossom = Blossom(v_value, w_value, v_root)
                            graph_clone = graph.clone()
                            matching_clone = matching.clone()
                            contraction = blossom.contract_graph(graph_clone)
                            blossom.contract_graph(matching_clone)
                            path = self.find_augmenting_path(graph_clone, matching_clone)
                            blossom.lift_path(path, contraction)
                            return path
                marked.append_pair(v_value, w_value)
            marked.append_value(v_value)
        return Path()