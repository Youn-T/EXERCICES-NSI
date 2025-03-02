def nombre_mystère():
    for i in range(100,300):
        if (i%2 == 0):
            if (chiffresIdentiques(i)):
                if (sommeChiffres(i) == 7):
                    return i
def chiffresIdentiques(nb):
    nbListe=list(str(nb))
    return (nbListe.count(nbListe[0]) == 2 or nbListe.count(nbListe[1]) == 2)

def sommeChiffres(nb):
    nbListe=list(str(nb))
    somme=0
    for elt in nbListe:
        somme+=int(elt)
    return somme

nombre_mystère()