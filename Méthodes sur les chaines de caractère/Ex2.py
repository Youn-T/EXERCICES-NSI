voyelles= ['a','e','i','o','u','y']
mot = "bonjour"
nvMot=""
for elt in mot:
    nvMot+=elt
    if (elt in voyelles):
        nvMot+=elt
        
print(nvMot)