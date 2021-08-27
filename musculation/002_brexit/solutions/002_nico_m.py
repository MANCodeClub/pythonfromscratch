import sys 

def affiche_drapeau(demi_taille):
    #demi_taille = int (input("donner la demi_taille du drapeau souhaité : "))
    T = demi_taille
    NbXModMax="" #j'initie une variable de type string qui va correspondre au nombre maximum de X accolés en fonction de la taille du drapeau.
    Car_Space="" #j'initie une variable de type string qui va correspondre à ligne vide de symétrie d'une longueur variant en fonction de la taille du drapeau.
    for i in range (T-1) : #pour un tableau de demi-taille=T, nombre de X accolés = T-1
        NbXModMax=NbXModMax+"X" 
    #    print (NbXModMax)
    # print (NbXModMax)

    for i in range (T) : #pour un tableau de demi-taille=T, j'affiche les lignes 1 à T
        Ligne_Haut = "|" + NbXModMax[:i] + " " + NbXModMax[i:T] + " " + NbXModMax[i:T] + " " + NbXModMax[:i] + "|"
        #print (NbXModB)
        print (Ligne_Haut)


    for i in range (2*T+1) : #pour un tableau de demi-taille=T, je dimensionne la ligne T+1 vide horizontale de symétrie (2T+1 d'espaces)
        Car_Space=Car_Space + " "

    Ligne_vide="|" + Car_Space + "|"

    print (Ligne_vide) #pour un tableau de demi-taille=T, j'affiche la ligne vide horizontale de symétrie


    for i in range (T) : #pour un tableau de demi-taille=T, j'affiche les lignes T+2 à 2xT+1
        Ligne_Bas = "|" + NbXModMax[i:T] + " " + NbXModMax[:i] + " " + NbXModMax[:i] + " " + NbXModMax[i:T] + "|"
        print (Ligne_Bas)

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