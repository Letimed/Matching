from joueurs import Joueur
from PlayerParser import parseString
from hop import HopcroftKarp
import math
import copy 
from Graph import Graph
from Vertex import Vertex
from Edge import Edge
import collections

"""
    Read dataset in data.csv and parse all data to create a list of players
"""
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

"""
    Perform ponderation on the player dataset
"""
def ponderate(playerList):
    for player in playerList:
        player._Dwinrate *= 1.5
        player._Dkda *= 0.8
        player._Dhonor *= 1.2
        player._Dreport *= 1.2
        player._Dafk *= 1.3
        player._Dratevictory *= 2


ponderate(playerList)

"""
    Create dataset partitions ( those will be used later to find maximum matching )
"""
team_1 = [player for player in playerList if player._team == 0]
team_2 = [player for player in playerList if player._team == 1]


graph = Graph()

""" 
    Build the graph vertexes using the team_1 and team_2 dataset
"""
for idx, player in enumerate(playerList):
    graph.add_vertex(Vertex(idx))

""" 
    Compute euclidian distance between vertexes and create an edge between them is distance is less than 1.5
"""
for pt1 in team_1:
    for pt2 in team_2:

        distance = (pt1._Dwinrate - pt2._Dwinrate) ** 2
        distance += (pt1._Dkda - pt2._Dkda) ** 2
        distance += (pt1._Dhonor - pt2._Dhonor) ** 2
        distance += (pt1._Dreport - pt2._Dreport) ** 2
        distance += (pt1._Dafk - pt2._Dafk) ** 2
        distance += (pt1._Dratevictory - pt2._Dratevictory) ** 2

        distance = math.sqrt(distance)

        if distance < 0.8:
            graph.add_edge(graph.find_vertex(pt1._idPlayer), graph.find_vertex(pt2._idPlayer))

"""
    Perform bipartite matching on the resulting graph
"""
hp = HopcroftKarp(graph, team_1, team_2)
print(str(hp.match()) + " matching !")


