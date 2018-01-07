from joueurs import Joueur
from PlayerParser import parseString
from makeGame import createGame
import math
import copy 
from Graph import Graph
from Vertex import Vertex
from Algo import Algo
from Edge import Edge

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

def bfs(graph, unmatched_1, unmatched_2):
    found = []

    for player in unmatched_1:
        vertex = graph.find_vertex(player._idPlayer)
        if vertex.degree() > 0:
            for edge in iter(vertex.edges.values()):
                peer = edge.w if edge.w != vertex.value else edge.v
                for player_2 in unmatched_2:
                    if player_2._idPlayer == peer.value:
                        if player_2._idPlayer not in found:
                            found.append(player_2._idPlayer)

    return found

def dfs(graph):
    return None
    
def hopcroft_karp(graph, team_1, team_2):
    m = Graph()

    p = bfs(graph.clone(), team_1, team_2) 

    print(len(team_2))
    print(len(p))

    print (p)

    ## bfs(graph.clone(), unmatched_1, unmatched_2)

    print ("Unmatched_1 : " + str(len(unmatched_1)))
    print ("Unmatched_2 : " + str(len(unmatched_2)))
    print ("Matched : " + str(len(p.vertices)))

hopcroft_karp(graph, team_1, team_2)
