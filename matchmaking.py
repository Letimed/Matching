from joueurs import Joueur
from PlayerParser import parseString
from makeGame import createGame
from hop import HopcroftKarp
import math
import copy 
from Graph import Graph
from Vertex import Vertex
from Algo import Algo
from Edge import Edge
import collections

# DATA CREATION

file = open("data.csv","r")
line = file.readline()
playerList = []
serverTab = ['Europe','Chine','Russie','Turquie']

while line  != "":
	player = parseString(line)
	playerList.append(player)
	line = file.readline()

minWinrate = min(float(player._winrate) for player in playerList)
maxWinrate = max(float(player._winrate) for player in playerList)
minKda = min(float(player._kda) for player in playerList)
maxKda = max(float(player._kda) for player in playerList)
minHonor = min(float(player._AvgHonor) for player in playerList)
maxHonor = max(float(player._AvgHonor) for player in playerList)
minReport = min(float(player._AvgReport) for player in playerList)
maxReport = max(float(player._AvgReport) for player in playerList)
minAfk = min(float(player._pctafk) for player in playerList)
maxAfk = max(float(player._pctafk) for player in playerList)
minRatevictory = min(float(player._ratevictory) for player in playerList)
maxRatevictory = max(float(player._ratevictory) for player in playerList)

for player in playerList:
	player.setStats(minWinrate, maxWinrate, minKda, maxKda, minHonor, maxHonor, minReport, maxReport, minAfk, maxAfk, minRatevictory, maxRatevictory)

#END DATA CREATION

matching = []

team_1 = [player for player in playerList if player._team == 0]
team_2 = [player for player in playerList if player._team == 1]

algo = Algo()
graph = Graph()

for idx, player in enumerate(playerList):
    graph.add_vertex(Vertex(idx))

for pt1 in team_1:
    for pt2 in team_2:

        distance = (pt1._Dwinrate - pt2._Dwinrate) ** 2
        distance += (pt1._Dkda - pt2._Dkda) ** 2
        distance += (pt1._Dhonor - pt2._Dhonor) ** 2
        distance += (pt1._Dreport - pt2._Dreport) ** 2
        distance += (pt1._Dafk - pt2._Dafk) ** 2
        distance += (pt1._Dratevictory - pt2._Dratevictory) ** 2

        distance = math.sqrt(distance)
        
        if distance < 0.5:
            graph.add_edge(graph.find_vertex(pt1._idPlayer), graph.find_vertex(pt2._idPlayer))

hp = HopcroftKarp(graph, team_1, team_2)
print("Matched : " + str(hp.match()))
exit()


def graph_bfs(graph, unmatched_1, unmatched_2):
    return None


def bfs(graph, unmatched_1, unmatched_2):
    found = []
    current_layer = [player._idPlayer for player in unmatched_1]
    next_layer = []

    while len(found) <= 0:
        for id in current_layer:
            vertex = graph.find_vertex(id)
            if vertex.degree() > 0:
                for edge in iter(vertex.edges.values()):
                    peer = edge.w if edge.w != vertex.value else edge.v
                    next_layer.append(peer.value)
                    for player_2 in unmatched_2:
                        if player_2._idPlayer == peer.value:
                            if player_2._idPlayer not in found:
                                found.append(player_2._idPlayer)
        current_layer = next_layer
        next_layer = []

    return found

def dfs(graph, unmatched_1, vertex):

    for edge in iter(vertex.edges.values()):
        path = Graph()
        peer = edge.w if edge.w != vertex.value else edge.v

        for player_1 in unmatched_1:
            if player_1._idPlayer == peer.value:
                print("found it !")
        
    
def hopcroft_karp(graph, team_1, team_2):

    g = Graph()
    unmatched_1 = team_1

    ## Get the nodes from V (team_2) reachable by bfs
    F = bfs(graph.clone(), team_1, team_2) 

    print(F)

    ## Try to reach an unmatched vertex from U (team_1) from F[x] to 
    for vertex in F:
        g = dfs(graph, unmatched_1, graph.find_vertex(vertex))


