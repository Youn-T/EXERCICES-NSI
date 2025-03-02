nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
debut=nombres[:round(len(nombres)/2)]
fin=nombres[round(len(nombres)/2):]

debut.reverse()
fin.reverse()

liste_transformee = debut + fin
print(liste_transformee)