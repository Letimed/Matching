

class Joueur(object):

    def __init__(self, nbwin, nblose, nbtotalgame, tempsmoyennesparties, kill, death, assist, honor, report, gametime, ratevictory, pctafk, nationalite):
        self._nbwin = nbwin
        self._nblose = nblose
        self._nbtotalgame = nbtotalgame
        self._tempsmoyenneparties = tempsmoyennesparties
        self._kill = kill
        self._death = death
        self._assist = assist
        self._honor = honor
        self._report = report
        self._gametime = gametime
        self._ratevictory = ratevictory
        self._pctafk = pctafk
        self._nationalite = nationalite
        self._skillScore = 0

    def printdatas(self):
        print("Player : " + str(self._nbwin)+';'+str(self._nblose)+';'+str(self._nbtotalgame)+';'+str(self._tempsmoyenneparties)+';'+str(self._kill)+';'+str(self._death)+';'+str(self._assist)+';'+str(self._honor)+';'+str(self._report)+';'+str(self._gametime)+';'+str(self._ratevictory)+';'+str(self._pctafk)+';'+str(self._nationalite)+'\n')

