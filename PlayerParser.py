from joueurs import Joueur


def parseString(myLine):
	idPlayer,team,nbwin,nblose,nbtotalgame,tempsmoyennesparties,kill,death,assist,honor,report,ratevictory,pctafk,nationalite,gold,gameCurrency = myLine.split(';')
	currentPlayer = Joueur(idPlayer,team,nbwin,nblose,nbtotalgame,tempsmoyennesparties,kill,death,assist,honor,report,ratevictory,pctafk,nationalite,gold,gameCurrency)
	return currentPlayer
