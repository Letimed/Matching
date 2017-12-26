import csv
from random import shuffle

pseudo=[]
nbwin=[str(i) for i in range(1,2000)]
nblose=[str(i) for i in range(1,2000)]
nbtotalgame=[nblose + nbwin]
tempsmoyennesparties=[str(i) for i in range(15,70)]
kill=[str(i) for i in range(1,70)]
death=[str(i) for i in range(1,70)]
assist=[str(i) for i in range(1,70)]
honor=[str(i) for i in range(1,2000)]
report=[str(i) for i in range(1,2000)]
gametime=[str(i) for i in range(1,100000)]
ratevictory=[str(i) for i in range(1,100)]
pctafk=[str(i) for i in range(1,100)]

def main():
    matrix = [nw+";"+nl+";"+ntg+";"+tmp+";"+k+";"+d+";"+a+";"+h+";"+r+";"+gt+";"+rv+";"+pca+"\n" for nw in nbwin for nl in nblose for ntg in nbtotalgame for tmp in tempsmoyennesparties for k in kill for d in death for a in assist for h in honor for r in report for gt in gametime for rv in ratevictory for pca in pcafk]
    shuffle(matrix)
    f = open("data.csv","w")
    for x in matrix[:25]:
        f.write(x)
    f.close()
