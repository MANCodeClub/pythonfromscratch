import sys

def affiche_drapeau(demi_taille):
    drapeau = ["|"] * (2 * demi_taille + 1) 
    for i in range(demi_taille):
        line = "|"
        for c in range(2 * demi_taille + 1):
            if c == i or c == demi_taille or c == 2 * demi_taille - i:
                line += " "
            else:
                line += "X"
        line += "|"
        drapeau[i] = line
        drapeau[-1-i] = line
    drapeau[demi_taille] = "|" + " " * (demi_taille*2+1) + "|"
    
    for line in drapeau:
        print(line)

""" En fusionnant les solutions des 2 Nicos on obtient ceci:"""
def affiche_drapeau_2(demi_taille):
    drapeau = ["|"] * (2 * demi_taille + 1) 
    for i in range(demi_taille):
        line = "|" + "X" * i + " " + "X" * (demi_taille-i-1) + " " + "X" * (demi_taille-i-1) + " " + "X" * i + "|"
        drapeau[i] = line
        drapeau[-1-i] = line
    drapeau[demi_taille] = "|" + " " * (demi_taille*2+1) + "|"
    
    for line in drapeau:
        print(line)

"""Au démarrage du programme sys.argv est une liste contenant tous les paramètres transmis par la ligne de commande.
argv[0] est le nom du script et on espère avoir le demi-coté dans argv[1]."""
if len(sys.argv) != 2:
    print("Indiquer le demi coté en paramètre:")
    print("Par exemple:")
    print("> python solve.py 5")
    exit(1)

demi_taille = int(sys.argv[1])
affiche_drapeau(demi_taille)
affiche_drapeau_2(demi_taille)
