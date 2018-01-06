class Path:

	def __init__(self):
		self.edges = []

	def __str__(self):
		return '\n'.join([str(x) for x in \
		 ["Path {"] + self.edges + ["}"]])

#   def discover_path(self, graph, value_start, value_end):
#       vertex_start = graph.find_vertex(value_start)
#       value_end = graph.find_vertex(value_end)
#       assert(vertex_start is not None)
#       assert(vertex_end is not None)
#       paths_start = {}
#       paths_end = {}
#       while True:
#           paths_start
