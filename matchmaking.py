from joueurs import Joueur
from PlayerParser import parseString
from makeGame import createGame

file = open("data.csv","r")
line = file.readline()
playerGraph = []
serverTab = ['Europe','Chine','Russie','Turquie']

while line  != "":
	player = parseString(line)
	playerGraph.append(player)
	line = file.readline()

createGame(playerGraph)