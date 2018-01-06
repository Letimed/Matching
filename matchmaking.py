from joueurs import Joueur
from PlayerParser import parseString
from makeGame import createGame
import math


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

# Compute euclidian distance and create graph
for idx_player, player in enumerate(playerList):

    matched = []

    # Iterate over all other player
    for idx_peer, peer in enumerate(playerList):

        # If we are comparing with the same player just skip to the next
        # element
        if peer == player:
            continue

        distance = (player._Dwinrate - peer._Dwinrate) ** 2
        distance += (player._Dkda - peer._Dkda) ** 2
        distance += (player._Dhonor - peer._Dhonor) ** 2
        distance += (player._Dreport - peer._Dreport) ** 2
        distance += (player._Dafk - peer._Dafk) ** 2
        distance += (player._Dratevictory - peer._Dratevictory) ** 2

        distance = math.sqrt(distance)
        
        # If the distance is beneath a certain treshold this is a similarity
        # So push it into the similarities graph
        if distance < 0.45:
            matched.append(peer._idPlayer)

    # Push the edges of that player
    matching.append(matched)

# print generated graph
for idx, entry in enumerate(matching):
    print("Matching [" + str(idx) + "] " + str(entry))


# ALGO

#createGame(playerList)

# END ALGO
