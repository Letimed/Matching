from joueurs import Joueur


def parseString(myLine):
	nbwin,nblose,nbtotalgame,tempsmoyennesparties,kill,death,assist,honor,report,gametime,ratevictory,pctafk,nationalité = myLine.split(';')
	currentPlayer = Joueur(nbwin,nblose,nbtotalgame,tempsmoyennesparties,kill,death,assist,honor,report,gametime,ratevictory,pctafk,nationalité)
	return currentPlayer