def trier(L):
    sortedList=[]
    while L != []:
        sortedList.append(min(L))
        L.remove(min(L))
    return sortedList

def doublons(L):
    newList=[]
    for elt in L:
        if not elt in newList:
            newList.append(elt)
    return trier(newList)

doublons([5, 1, 1, 2, 5, 6, 3, 4, 4, 4, 2])