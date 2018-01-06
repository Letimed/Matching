class Marked:
  def __init__(self):
    self.node_values = {}
    self.node_pairs = {}

  def append_value(self, value):
    self.node_values[value] = 1
  
  def append_pair(self, v, w):
    if v not in self.node_pairs:
      self.node_pairs[v] = {}
      self.node_pairs[v][w] = 1
  
  def has_value(self, value):
    return value in self.node_values
  
  def has_pair(self, v, w):
    return self.test_has_pair(v, w) or self.test_has_pair(w, v)
  
  def test_has_pair(self, v, w):
    return v in self.node_pairs and w in self.node_pairs[v] and self.node_pairs[v][w] == 1