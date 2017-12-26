from random import shuffle

nbwin=[str(i) for i in range(1,2000)]
nblose=[str(i) for i in range(1,2000)]
nbtotalgame=nblose + nbwin
kill=[str(i) for i in range(1,70)]
death=[str(i) for i in range(1,70)]
assist=[str(i) for i in range(1,70)]
honor=[str(i) for i in range(1,2000)]
report=[str(i) for i in range(1,2000)]
gametime=[str(i) for i in range(1,100000)]
ratevictory=[str(i) for i in range(1,100)]
pctafk=[str(i) for i in range(1,100)]
nationalité=[str(i) for i in range(1,10)]

print nbwin

matrix = [nw+";"+nl+";"+tmp+";"+k+";"+d+";"+a+";"+h+";"+r+";"+gt+";"+rv+";"+pca+";"+na+"\n" for nw in nbwin for nl in nblose for tmp in tempsmoyennesparties for k in kill for d in death for a in assist for h in honor for r in report for gt in gametime for rv in ratevictory for pca in pctafk for na in nationalité]
shuffle(matrix)
f = open("data.csv","w")
for x in matrix[:25]:
    f.write(x)
f.close()
