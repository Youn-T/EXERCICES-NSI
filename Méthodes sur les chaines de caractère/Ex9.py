def remplacer_voyelle(chaine, v1,v2):
    voyelles= ['a','e','i','o','u','y']
    
    if (not (v1 in voyelles) or not (v2 in voyelles)) :
        return chaine
    return chaine.replace(v1,v2)

chaine = "abracadabra"  
v1 = "a"  
v2 = "o"  
resultat = remplacer_voyelle(chaine, v1, v2)
print(resultat)