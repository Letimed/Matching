from joueurs import Joueur


def parseString(myLine):
	nbwin,nblose,nbtotalgame,tempsmoyennesparties,kill,death,assist,honor,report,gametime,ratevictory,pctafk,nationalite = myLine.split(';')
	currentPlayer = Joueur(nbwin,nblose,nbtotalgame,tempsmoyennesparties,kill,death,assist,honor,report,gametime,ratevictory,pctafk,nationalite)
	return currentPlayer