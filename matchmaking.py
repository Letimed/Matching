from joueurs import Joueur
from PlayerParser import parseString
from makeGame import createGame

file = open("data.csv","r")
line = file.readline()
playerGraph = []

while line  != "":
	player = parseString(line)
	playerGraph.append(player)
	line = file.readline()

playerGraph.sort(key=lambda x: x._elo, reverse=False)
createGame(playerGraph)