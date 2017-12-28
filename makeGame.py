from joueurs import Joueur


def printTeam(myTeam, teamName):
	print(teamName)
	a = 0
	while a < len(myTeam):
		myTeam[a].printdatas()
		a = a + 1
	print('\n')

def createGame(myPlayerGraph):
	currentPlayer = 0
	gameNumber = 1
	while gameNumber <= len(myPlayerGraph) / 10:
		print("Game Number "+ str(gameNumber) + " : \n")
		team1 = []
		team2 = []
		while (len(team1) < 5 and len(team2) < 5):
			team1.append(myPlayerGraph[currentPlayer])
			currentPlayer = currentPlayer + 1
			team2.append(myPlayerGraph[currentPlayer])
			currentPlayer = currentPlayer + 1
		printTeam(team1, "Blue Team :")
		printTeam(team2, "Red Team :")
		gameNumber = gameNumber + 1