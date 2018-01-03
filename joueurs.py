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
        self._skillScore = 0
        self._fairPlayScore = 0
        self.makeScore()

    def printdatas(self):
        print("Player : "+ str(self._idPlayer)+ ';'+ str(self._nbwin)+';'+str(self._nblose)+';'+str(self._nbtotalgame)+';'+str(self._tempsmoyenneparties)+';'+str(self._kill)+';'+str(self._death)+';'+str(self._assist)+';'+str(self._honor)+';'+str(self._report)+';'+';'+str(self._ratevictory)+';'+str(self._pctafk)+';'+str(self._nationalite)+';'+str(self._gold)+';'+str(self._gameCurrency)+';'+str(self._skillScore)+';'+str(self._fairPlayScore))

    def makeSkillScore(self):
        kdaCoef = 1
        ratioWinrateCoef = 1
        kdaRating = ((self._kill + self._assist) / self._death) / 40
        ratiowinrateRating = self._nbwin / self._nbtotalgame / 100
        self._skillScore = ((kdaRating * kdaCoef)  + (ratiowinrateRating * ratioWinrateCoef)) / (kdaCoef + ratioWinrateCoef)

    def makeFairPlayScore(self):
        ratiohonorCoef = 1
        ratioreportCoef = 1
        afkCoef = 1
        ratiohonor = self._honor / self._nbtotalgame 
        ratioreport =  1 - (self._report / self._nbtotalgame)
        ratioAfk = 1 - (self._pctafk / 100)
        self._fairPlayScore = ((ratiohonor * ratiohonorCoef) + (ratioreport * ratioreportCoef) + (ratioAfk * afkCoef) )/ (ratiohonorCoef + ratioreportCoef + afkCoef) 

    def makeScore(self):
        self.makeSkillScore()
        self.makeFairPlayScore()