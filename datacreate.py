from random import randint

f = open("data.csv","w")
a = 0
while a < 200:
	elo=randint(0,4000)
	nbwin=randint(0,2000)
	nblose=randint(0,2000)
	nbtotalgame=nblose + nbwin
	tempsmoyennesparties=randint(15,70)
	kill=randint(0,70)
	death=randint(0,70)
	assist=randint(0,70)
	honor=randint(0,2000)
	report=randint(0,2000)
	gametime=randint(0,100000)
	ratevictory=randint(0,100)
	pctafk=randint(0,100)
	nationalite=randint(1,10)
	
	f.write(str(elo)+';'+str(nbwin)+';'+str(nblose)+';'+str(nbtotalgame)+';'+str(tempsmoyennesparties)+';'+str(kill)+';'+str(death)+';'+str(assist)+';'+str(honor)+';'+str(report)+';'+str(gametime)+';'+str(ratevictory)+';'+str(pctafk)+';'+str(nationalite)+'\n')
	a = a + 1
f.close()
