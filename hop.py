#Algorithms for bipartite graphs

from joueurs import Joueur
from Graph import Graph
from Vertex import Vertex
from Edge import Edge
import collections

class HopcroftKarp(object):

    def __init__(self, G, team_1, team_2):
        """ 
            G: the graph received as implemented in Graph.py and Edge.py
            team_1: the data structure holding every player in team_1
            team_2: the data structure holding every player in team_2
        """
        self.G = G
        self.team_1 = team_1
        self.team_2 = team_2

    def getPartition(self, team):
        """
            team: the team ( self.team_1 or self.team_2 )
            Find and aggregate all the vertex representing players from the supplied team.
            This allow the recuperation of a partition of the graph from the dataset

            Returns: partition: a list of vertex
        """
        partition = []
        for player in team:
                partition.append(self.G.find_vertex(player._idPlayer))
        return partition

    def match(self):
        """
            Perform a bipartite matching on the graph self.G by calling repeatedly
            bfs and dfs function to look for amelioration matching
        """

        """
            Init the required data structures :
                - Get the graph partitions for team_1 and team_2
                - Init the pairs to an empty dict
                - Init the distances to an empty dict
                - Init the queue
        """
        self.N1 = self.getPartition(self.team_1)
        self.N2 = self.getPartition(self.team_2)
        self.pair = {}
        self.dist = {}
        self.q = collections.deque()

        """
            Init every vertex in self.G setting its pairs and distances to None
            and infinity respectively. This allow a clean startup of the main loop
        """
        for v in self.G.vertices:
            self.pair[v] = None
            self.dist[v] = float("inf")

        matching = 0

        while self.bfs():
            for v in self.N1:
                """ If node is unmatched and dfs found a path for it then a match is found """
                if self.pair[v] is None and self.dfs(v):
                    matching = matching + 1

        """ Simple print routine for ( bad ) visualisation of the matching """
        for vertex in iter(self.pair.values()):
            if vertex is not None:
                print(str(vertex) + " -> " + str(self.pair[vertex]))
        return matching

    def dfs(self, v):
        """
            Create an alternating path from an augmenting path found by bfs
        """
        if v != None:
            for u in v.getNeighbors():
                """ A shortest augmenting path was found create alternating path """
                if self.dist[ self.pair[u] ] == self.dist[v] + 1 and self.dfs(self.pair[u]):
                    self.pair[u] = v
                    self.pair[v] = u
                    return True
            """ No shortest augmenting path was found """
            self.dist[v] = float("inf")
            return False

        return True

    def bfs(self):
        """
            Perform a breadth first search to find augmenting path from unmatched nodes in self.N1
            to unmatched nodes in self.N2. While doing so the distance to the different nodes from
            the source is updated so that dfs can create a shortest alternating path from it
        """

        """ Push each unmatched node in self.N1 to the queue """
        for v in self.N1:
            if self.pair[v] == None:
                self.dist[v] = 0
                self.q.append(v)
            else:
                self.dist[v] = float("inf")

        """ 
            Mark the "dummy" node "in" self.N2 as unreached by the bfs checking this value later
            tells us if we found an augmenting path
        """
        self.dist[None] = float("inf")

        while len(self.q) > 0:
            v = self.q.popleft()
            if v != None:
                for u in v.getNeighbors():
                    if self.dist[ self.pair[u] ] == float("inf"):
                        self.dist[ self.pair[u] ] = self.dist[v] + 1
                        self.q.append(self.pair[u])

        """ True when at least one path was found """
        return self.dist[None] != float("inf")

