"""
1- Il est constitué de 7 chiffres
2- il ne commence pas par 0
3- Le dernier chiffre doit être le chiffre des unité de la somme des six premiers multipliés par le position +1

Zavez rien compris? On va faire un exemple:

Par exemple:
9876548

Par exemple:
9876548
1111117

On fait le calcul avec les 6 premiers chiffres:
9*2 + 8*3 + 7*4 + 6*5 + 5*6 + 4*7 = 158
1*2 + 1*3 + 1*4 + 1*5 + 1*6 + 1*7 = 27
"""
def clef (liste) :
    clef = 0
    n = 2
    for chiffre in liste[0:6] :
        clef = clef + chiffre * (n)
        n=n+1
        #print (clef)
    clef = str(clef)
    #print (clef)
    #print (len(clef))
    clef = clef[len(clef)-1:len(clef)] 
    clef = int(clef)
    #print (clef)
    """ NVI: Là ça a été dur on dirait ;-).
    Tu veux retourner le chiffre des unités, c'est le reste de la division par 10
    L'opérateur % (modulo) permet de retourner ce reste:
    reste = valeur % diviseur
    donc pour nous:
    return clef % 10 aurait suffit
    Comment ça j'aurais du le dire avant?!
    """
    return clef

def check_IMO_nbr(number) :
    liste_chiffre=[]
    number = str (number)
    for chiffre in number :
    #print (chiffre)
        liste_chiffre.append(int(chiffre))

    """ NVI il n'est pas utile de différencier les booléens premier_chiffre, longueur7 et clef_verif.
    Si le test ne passe pas il suffit d'arrêter la fonction et de retourner False
    if liste_chiffre[0] == 0 :
        return False
    if len(liste_chiffre) != 7 :
        return False
    if clef(liste_chiffre) != liste_chiffre[6]:
        return False

    On peut aussi tout regrouper dans le même test si ça reste lisible.
    """
    if liste_chiffre[0] != 0 :
        premier_chiffre = True
    else :
        premier_chiffre = False

    if len(liste_chiffre) == 7 :
        longueur7 = True
    else :
        longueur7 = False

    if len(liste_chiffre)==7 and clef(liste_chiffre) == liste_chiffre[6] :
        clef_verif = True
    else :
        clef_verif = False

    #print (premier_chiffre)
    #print(longueur7)
    #print (clef(liste_chiffre))
    #print (clef_verif)
    if (premier_chiffre is True) and (longueur7 is True) and (clef_verif is True) :
        resultat = True
    else :
        resultat = False
    #print (resultat)
    return resultat

def check_IMO_field(field) :
    test = True
    try :
        field=int(field)
    except  ValueError :
        test = False
    if test is True :
        resultat = check_IMO_nbr(field)
    elif test is False :
        resultat = False
    return (resultat)