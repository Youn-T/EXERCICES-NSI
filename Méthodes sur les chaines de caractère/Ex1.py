phrase="La brosse à dents bleue"

nouvellePhrase = phrase[0]
for elt in phrase[1:-2]:
    nouvellePhrase+= "%"+elt
    
print(nouvellePhrase)