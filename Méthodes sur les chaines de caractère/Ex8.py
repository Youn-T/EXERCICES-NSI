phrase = "Python est un langage fascinant"  
liste=phrase.split()
maxi=liste[0]
for i in range(len(liste)):
    if (len(maxi) < len(liste[i])):
        maxi=liste[i]
print(maxi)