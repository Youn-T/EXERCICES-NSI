phrase = "La brosse à dents bleue"
mot = "serpent"

phraseFinale=""
correction=0

for i in range(len(phrase)):
    if (i-correction==len(mot)):
        correction+= len(mot)
    phraseFinale+=phrase[i] + mot[i-correction]
    
print(phraseFinale)