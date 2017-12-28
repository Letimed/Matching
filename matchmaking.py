from joueurs import Joueur
from PlayerParser import parseString

file = open("data.csv","r")
line = file.readline()
playerList = []
playerOrganised{}
while line  != "":
	player = parseString(line)
	playerList.append(player)
	line = file.readline()

a = 0
while a < 200:
	playerList[a].printdatas()
	a = a + 1
