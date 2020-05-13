import math

def weight(locDistribute):
    infoList=[]
    locList = locDistribute.split(',')
    locTotal = 0;
    for loc in locList:
        locTotal+= int(loc)
    for loc in locList:
        infoList.append(round(int(loc)/locTotal,3))
    return infoList

def entropy(infoList):
    entropy = 0
    for info in infoList:
        entropy+= info*math.log(info,math.e)
    return -entropy

if __name__ == "__main__":
    print("Please input loc of each task split by ,")
    storyWorklad = input("input:")
    entropy = entropy(weight(storyWorklad))
    print(entropy)
    