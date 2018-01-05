class Joueur(object):

    def __init__(self, idPlayer, nbwin, nblose, nbtotalgame, tempsmoyennesparties, kill, death, assist, honor, report, ratevictory, pctafk, nationalite,gold,gameCurrency):
        self._idPlayer = int(idPlayer)
        self._nbwin = int(nbwin)
        self._nblose = int(nblose)
        self._nbtotalgame = int(nbtotalgame)
        self._tempsmoyenneparties = int(tempsmoyennesparties)
        self._kill = int(kill)
        self._death = int(death)
        self._assist = int(assist)
        self._honor = int(honor)
        self._report = int(report)
        self._ratevictory = int(ratevictory)
        self._pctafk = int(pctafk)
        self._nationalite = int(nationalite)
        self._gold = int(gold)
        self._gameCurrency = int(gameCurrency)
        self._winrate = self._nbwin / self._nbtotalgame
        self._kda = (self._kill + self._assist) / self._death
        self._AvgHonor = self._honor / self._nbtotalgame
        self._AvgReport = self._report / self._nbtotalgame
        self._Dwinrate = -1
        self._Dkda = -1
        self._Dhonor = -1
        self._Dreport = -1
        self._Dafk = -1
        self._Dratevictory = -1

    def printdatas(self):
        print("Player : "+ str(self._idPlayer)+ ';'+ str(self._nbwin)+';'+str(self._nblose)+';'+str(self._nbtotalgame)+';'+str(self._tempsmoyenneparties)+';'+str(self._kill)+';'+str(self._death)+';'+str(self._assist)+';'+str(self._honor)+';'+str(self._report)+';'+';'+str(self._ratevictory)+';'+str(self._pctafk)+';'+str(self._nationalite)+';'+str(self._gold)+';'+str(self._gameCurrency))

    def setStats(self, minWinrate, maxWinrate, minKda, maxKda, minHonor, maxHonor, minReport, maxReport, minAfk, maxAfk, minRatevictory, maxRatevictory):
        self._Dwinrate = (self._winrate - minWinrate) / (maxWinrate - minWinrate)
        self._Dkda = (self._kda - minKda) / (maxKda - minKda)
        self._Dhonor = (self._AvgHonor - minHonor) / (maxHonor - minHonor)
        self._Dreport = (self._AvgReport - minReport) / (maxReport - minReport)
        self._Dafk = (self._pctafk - minAfk) / (maxAfk - minAfk)
        self._Dratevictory = (self._ratevictory - minRatevictory) / (maxRatevictory - minRatevictory)

    def makeScore(self):
        self.makeSkillScore()
        self.makeFairPlayScore()