lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# print(lettres[:3])
# print(lettres[-3:])
# print(lettres[2:6])

def inverser():
    global lettres
    
    fin=lettres[:][-1:]
    debut=lettres[:][:1]
    lettres[:1]=fin
    lettres[-1:]=debut
    
    for i in range(1,round(len(lettres)/2)):
        fin=lettres[:][-(i+1):-i]
        debut=lettres[:][i:i+1]
        lettres[-(i+1):-i] = debut
        lettres[i:i+1] = fin

inverser()
print(lettres)