#Algorithms for bipartite graphs

from joueurs import Joueur
from Graph import Graph
from Vertex import Vertex
from Edge import Edge
import collections

class HopcroftKarp(object):
    INFINITY = -1

    def __init__(self, G, team_1, team_2):
        self.G = G
        self.team_1 = team_1
        self.team_2 = team_2

    def getPartition(self, team):
        partition = []
        for player in team:
                partition.append(self.G.find_vertex(player._idPlayer))
        return partition

    def match(self):
        self.N1 = self.getPartition(self.team_1)
        self.N2 = self.getPartition(self.team_2)
        self.pair = {}
        self.dist = {}
        self.q = collections.deque()

        #init
        for v in self.G.vertices:
            self.pair[v] = None
            self.dist[v] = HopcroftKarp.INFINITY

        matching = 0

        while self.bfs():
            for v in self.N1:
                if self.pair[v] is None and self.dfs(v):
                    matching = matching + 1

        for vertex in iter(self.pair.values()):
            if vertex is not None:
                print(str(vertex) + " -> " + str(self.pair[vertex]))
        return matching

    def dfs(self, v):
        if v != None:
            for u in v.getNeighbors():
                if self.dist[ self.pair[u] ] == self.dist[v] + 1 and self.dfs(self.pair[u]):
                    self.pair[u] = v
                    self.pair[v] = u

                    return True

            self.dist[v] = HopcroftKarp.INFINITY
            return False

        return True

    def bfs(self):
        for v in self.N1:
            if self.pair[v] == None:
                self.dist[v] = 0
                self.q.append(v)
            else:
                self.dist[v] = HopcroftKarp.INFINITY

        self.dist[None] = HopcroftKarp.INFINITY

        while len(self.q) > 0:
            v = self.q.popleft()
            if v != None:
                for u in v.getNeighbors():
                    if self.dist[ self.pair[u] ] == HopcroftKarp.INFINITY:
                        self.dist[ self.pair[u] ] = self.dist[v] + 1
                        self.q.append(self.pair[u])

        return self.dist[None] != HopcroftKarp.INFINITY

