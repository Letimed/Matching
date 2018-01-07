class Edge:

  def __init__(self, v, w):
    self.v = v
    self.w = w

  def other(self, v):
    if v == self.v:
      return self.w
    elif v == self.w:
      return self.v
    else:
      raise

  def __str__(self):
    return "<{}, {}>".format(str(self.v), str(self.w))

  def __repr__(self):
    return "Edge({}, {})".format(repr(self.v), repr(self.w))
