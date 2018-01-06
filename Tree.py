class Tree:

    def __init__(self, value, children, parent):
        self.value = value
        self.children = children
        self.parent = parent

    def add_child(self, value):
        tree = Tree(value, [], self)
        self.children.append(tree)
        return tree

    def subnodes(self):
        s = [self]
        for child in self.children:
            s += child.subnodes()
        return s

    def height(self):
        if self.parent == None:
            return 0
        else:
            return 1 + self.parent.height()

    def find(self, value):
        search = [self]
        while search:
            t = search[0]
            if t.value == value:
                return t
            else:
                search += t.children
                search = search[1:]
        return None

    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()

    def __str__(self):
        return "T[{} {}]".format(self.value, self.children)

    def __repr__(self):
        return "Tree({}, {})".format(self.value, self.children)
