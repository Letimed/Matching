from random import randint

f = open("data.csv","w")
idPlayer=0
while idPlayer < 200:
    team=randint(0,1)
    nbwin=randint(0,2000)
    nblose=randint(0,2000)
    nbtotalgame=nblose + nbwin
    tempsmoyennesparties=randint(15,70)
    kill=randint(0,20)
    death=randint(1,20)
    assist=randint(0,20)
    honor=randint(0,nbtotalgame)
    report=randint(0,nbtotalgame)
    if nbtotalgame < 20:
            ratevictory = nbwin / nbtotalgame * 100
    elif nbtotalgame > 20 and nbwin < 20:
            nbtotalgame = nbtotalgame + 40
            nbwin = nbwin + 20
            nblose = nblose + 20
            ratevictory=randint(0,100)
    else :
            ratevictory=randint(0,100)
    pctafk=randint(0,100)
    nationalite=randint(0,3)
    if nbtotalgame > 0:
            gold=randint(500,30000)
    else :
            gold=0
    gameCurrency = randint(0,100000)

    f.write(str(idPlayer)+';'+str(team)+';'+str(nbwin)+';'+str(nblose)+';'+str(nbtotalgame)+';'+str(tempsmoyennesparties)+';'+str(kill)+';'+str(death)+';'+str(assist)+';'+str(honor)+';'+str(report)+';'+str(ratevictory)+';'+str(pctafk)+';'+str(nationalite)+';'+str(gold)+';'+str(gameCurrency)+'\n')
    idPlayer = idPlayer + 1
f.close()
