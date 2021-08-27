import sys 

def affiche_drapeau(demi_taille):
    """ NVI: j'ai conservé ton algo tel quel mais j'ai simplement utilisé la syntaxe "X" * 4 qui permet de créer une chaîne "XXXX"
    de manière générale on peut initialiser des listes ou des chaînes de cette façon.
    par exemple pour initialiser une liste de n 0 on peut faire: l = [0] * n
    Par ailleurs, comme les expressions étaient plus simples j'ai aussi supprimé les variables intermédiaires.
    On peut sans doute faire encore plus simple effectivement avec les symétries mais on est déjà à un niveau de clareté suffisant maintenant"""

    """NVI: autre remarque qui ne se voit plus après mon ménage mais tu utilisais de noms de variables indiquant un nombre de X alors que le 
    contenu n'était pas un nombre. NbXModMax aurait pu s'appeler chaineX ou je ne sais quoi mais pas nb..."""

    """ NVI: Je trouve la ligne suivante un peu inutile mais on peut en discuter:
    Je comprends que le nom demi_taille est un peu long pour être inséré dans les calculs (discutable).
    On pourrait simplement changer le nom de l'argument de la fonction par T mais on l'utilisateur de la fonction ce serait moins clair"""
    T = demi_taille # NVI: Je trouve cette ligne un peu inutile mais 

    for i in range (T) : #pour un tableau de demi-taille=T, j'affiche les lignes 1 à T
        print( "|" + "X" * i + " " + "X" * (T-i-1) + " " + "X" * (T-i-1) + " " + "X" * i + "|")

    print("|" + " "*(2*T+1) + "|") #pour un tableau de demi-taille=T, j'affiche la ligne vide horizontale de symétrie

    for i in range (T) : #pour un tableau de demi-taille=T, j'affiche les lignes T+2 à 2xT+1
        print( "|" + "X" * (T-i-1) + " " + "X" * i + " " + "X" * i + " " + "X" * (T-i-1) + "|")

""" NVI: J'ai ajouté un contrôle du nombre de paramètre avec une explication en cas de mauvaise utilisation.
C'est sans doute ce qui t'as posé problème.
Au démarrage du programme sys.argv est une liste contenant tous les paramètres transmis par la ligne de commande.
argv[0] est le nom du script et on espère avoir le demi-coté dans argv[1]."""
if len(sys.argv) != 2:
    print("Indiquer le demi coté en paramètre:")
    print("Par exemple:")
    print("> python solve.py 5")
    exit(1)

demi_taille=int (sys.argv[1])
affiche_drapeau(demi_taille)


"""
> python solve.py 10
| XXXXXXXXX XXXXXXXXX |
|X XXXXXXXX XXXXXXXX X|
|XX XXXXXXX XXXXXXX XX|
|XXX XXXXXX XXXXXX XXX|
|XXXX XXXXX XXXXX XXXX|
|XXXXX XXXX XXXX XXXXX|
|XXXXXX XXX XXX XXXXXX|
|XXXXXXX XX XX XXXXXXX|
|XXXXXXXX X X XXXXXXXX|
|XXXXXXXXX   XXXXXXXXX|
|                     |
|XXXXXXXXX   XXXXXXXXX|
|XXXXXXXX X X XXXXXXXX|
|XXXXXXX XX XX XXXXXXX|
|XXXXXX XXX XXX XXXXXX|
|XXXXX XXXX XXXX XXXXX|
|XXXX XXXXX XXXXX XXXX|
|XXX XXXXXX XXXXXX XXX|
|XX XXXXXXX XXXXXXX XX|
|X XXXXXXXX XXXXXXXX X|
| XXXXXXXXX XXXXXXXXX |

Ligne 01     = 9X 0X 0X 9X
Ligne 02     = 8X 1X 1X 8X
Ligne 03     = 7X 2X 2X 7X
Ligne 04     = 6X 3X 3X 6X
Ligne 05     = 5X 4X 4X 5X
Ligne 06     = 4X 5X 5X 4X
Ligne 07     = 3X 6X 6X 3X
Ligne 08     = 2X 7X 7X 2X
Ligne 09     = 1X 8X 8X 1X
Ligne 10 | T = 0X 9X 9X 0X
Ligne 11 | T+1 = Null
Symétrie
"""