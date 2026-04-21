import random

#comment land
i=0
averagerolls = []


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
    specifi = 27
    chanceOf = averagerolls.count(specifi)
    chanceOf = chanceOf/10000
    chanceOf = chanceOf*100
    print(f"chance of {specifi}: {chanceOf}%")

    return

basicstats()