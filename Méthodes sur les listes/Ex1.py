def trier(L):
    sortedList=[]
    while L != []:
        sortedList.append(min(L))
        L.remove(min(L))
    return sortedList

trier([8, 3, 12.5, 45, 25.5, 52, 1])