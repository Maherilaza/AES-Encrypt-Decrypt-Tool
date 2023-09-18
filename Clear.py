import os
condition = True
while condition:
    print("J'espère que tu as copié tes clés, car ça va tout supprimer")
    file = input("> Supprimer ? o/n : ")
    if file == "o":
        condition = False

    elif file == "n":
        break
    else:
        print("Lol ..")
        break

dossier = "AES-EF"
temp = os.listdir(dossier)

for fichier in temp:
    chemin_fichier = os.path.join(dossier, fichier)

try:
    cle = "AES-C"
    os.remove(cle)
except FileNotFoundError:
    pass