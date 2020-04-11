import sys

def affiche_drapeau(demi_taille):
    # FIXME: remplacer le code de cette fonction
    print("devrait afficher le drapeau à la bonne taille")


"""Au démarrage du programme sys.argv est une liste contenant tous les paramètres transmis par la ligne de commande.
argv[0] est le nom du script et on espère avoir le demi-coté dans argv[1]."""
if len(sys.argv) != 2:
    print("Indiquer le demi coté en paramètre:")
    print("Par exemple:")
    print("> python solve.py 5")
    exit(1)

demi_taille = int(sys.argv[1])
affiche_drapeau(demi_taille)
