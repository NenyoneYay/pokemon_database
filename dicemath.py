import random
import numpy as np
import matplotlib.pyplot as plt

#comment land
i=0
averagerolls = []

statsum = []
strn = 0
dex = 0
con = 0
inte = 0
wis = 0
cha = 0


def rolling():
    mynumber = random.randrange(1,7)
    if(mynumber < 3):
        mynumber = random.randrange(1,7)
    return mynumber

def statTotal():
    mylist = []
    mylist.append(rolling())
    mylist.append(rolling())
    mylist.append(rolling())
    mylist.append(rolling())
    mylist.append(rolling())
    mylist.append(rolling())
    mylist.sort()
    #print(mylist)
    mylist.pop(0)
    #print(mylist)
    total = 0
    for result in range(len(mylist)): 
        total += mylist[result]
    #print(total)
    return total

while(i<10000):
   averagerolls.append(statTotal())
   statsum.append(statTotal()+statTotal()+statTotal()+statTotal()+statTotal()+statTotal())
   i += 1

averagerolls.sort()
#print(averagerolls)

#mean median mode
def basicstats():

    print(f"median: {averagerolls[5000]}")

    listaverage = 0
    listmean = 0
    for roll in range(len(averagerolls)):
        listaverage += averagerolls[roll]
    listmean = listaverage//len(averagerolls)
    listmean += 1
    listaverage = listaverage/len(averagerolls)
    print(f"average: {listaverage}")
    print(f"ceilinged average: {listmean}")

    #print(f"number of 16's {averagerolls.count(16)}")
    specifi = 16
    chanceOf = averagerolls.count(specifi)
    chanceOf = chanceOf/10000
    chanceOf = chanceOf*100
    print(f"chance of {specifi}: {chanceOf}%")

    return

basicstats()

xAxis = np.array(["6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"])
yAxis = np.array([averagerolls.count(6),averagerolls.count(7),averagerolls.count(8),averagerolls.count(9),averagerolls.count(10),averagerolls.count(11),averagerolls.count(12),averagerolls.count(13),averagerolls.count(14),averagerolls.count(15),averagerolls.count(16),averagerolls.count(17),averagerolls.count(18),averagerolls.count(19),averagerolls.count(20),averagerolls.count(21),averagerolls.count(22),averagerolls.count(23),averagerolls.count(24),averagerolls.count(25),averagerolls.count(26),averagerolls.count(27),averagerolls.count(28),averagerolls.count(29),averagerolls.count(30)])

standardDev = np.std(averagerolls)
print(standardDev)

statdev = np.std(statsum)
statmean = np.mean(statsum)
print(f"standard deviation: {statdev}")
print(f"stats mean: {statmean}")

#plt.bar(xAxis,yAxis)
#plt.show()
