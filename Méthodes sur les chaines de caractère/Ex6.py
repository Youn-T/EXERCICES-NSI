voyelles= ['a','e','i','o','u','y']
chaine = "programmation"  
voy=0
for voyelle in voyelles:
    voy += chaine.count(voyelle)

print(f"voyelles : {voy} consonnes : {len(chaine)-voy}")