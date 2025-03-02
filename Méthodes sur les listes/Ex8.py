def moyenne_liste(L):
    total = 0
    count=0
    for element in L:
        total += element
        count += 1
    return total/count

temperatures = [13, 15, 14, 18, 21, 20, 19, 17]
matin= temperatures[:4]
soir=temperatures[4:]
print(moyenne_liste(matin))
print(moyenne_liste(soir))