from joueurs import Joueur
from PlayerParser import parseString
from makeGame import createGame


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

# ALGO

#createGame(playerList)

# END ALGO