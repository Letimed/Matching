

class Joueur(object):

    def __init__(self, elo, nbwin, nblose, nbtotalgame, tempsmoyennesparties, kill, death, assist, honor, report, gametime, ratevictory, pctafk, nationalite):
        self._elo = int(elo)
        self._nbwin = int(nbwin)
        self._nblose = int(nblose)
        self._nbtotalgame = int(nbtotalgame)
        self._tempsmoyenneparties = int(tempsmoyennesparties)
        self._kill = int(kill)
        self._death = int(death)
        self._assist = int(assist)
        self._honor = int(honor)
        self._report = int(report)
        self._gametime = int(gametime)
        self._ratevictory = int(ratevictory)
        self._pctafk = int(pctafk)
        self._nationalite = int(nationalite)
        self._skillScore = 0

    def printdatas(self):
        print("Player : "+ str(self._elo)+ ';' + str(self._nbwin)+';'+str(self._nblose)+';'+str(self._nbtotalgame)+';'+str(self._tempsmoyenneparties)+';'+str(self._kill)+';'+str(self._death)+';'+str(self._assist)+';'+str(self._honor)+';'+str(self._report)+';'+str(self._gametime)+';'+str(self._ratevictory)+';'+str(self._pctafk)+';'+str(self._nationalite)+'\n')

