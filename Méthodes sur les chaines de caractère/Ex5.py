phrase = "La programmation est amusante."
listePhrase = phrase.split()
cnt=len(listePhrase)

nb3Points=phrase.count("...")
nbPoints=phrase.count(".") - 3*nb3Points

cnt+= nbPoints
cnt+= nb3Points

print(cnt)