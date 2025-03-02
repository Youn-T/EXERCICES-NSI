chaine = "python" 
chaineFinale=""
for i in range(len(chaine)):
    if (i%2==0):
        chaineFinale += chaine[i].upper()
    else:
        chaineFinale += chaine[i].lower()
        
print(chaineFinale)