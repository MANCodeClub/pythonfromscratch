FILE_PATH = "toto.txt"

# création du fichier
f = open(FILE_PATH, "w")
f.write("Première ligne\n")
f.write(f"{123456789}\n")  # on ne peut écrire que des str pas des int
f.write("3e ligne")
f.write(" suite de la 3e ligne\n")
f.close()

# ajout d'une ligne à la fin (append)
f = open(FILE_PATH, "a")
f.write("4e ligne")
f.close()

# lire tout d'un coup
f = open(FILE_PATH, "r")
contenu = f.read()
print(contenu)

# retour au début du fichier
f.seek(0)
# lire une ligne
line = f.readline()
print(line)
# lire la suite dans une liste de ligne
lines = f.readlines()
print(lines)
""" on constate au passage que les fins de ligne issues du fichier s'ajoute à celles de la fonction print()
    Dans l'exemple suivant on utilisera la methode strip() pour nettoyer les lignes lues dans le fichier.
"""


f.seek(0)
# lecture du fichier ligne à ligne en utilisant l'itérateur
for ligne in f:
    # on supprime les blanc et \n en fin de ligne.
    ligne = ligne.strip()
    print(ligne)
