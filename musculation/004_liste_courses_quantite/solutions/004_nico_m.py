FILE_PATH="./"
file_shopping = open(FILE_PATH+"liste_avec_doublons.txt","r")
shopping_liste=(file_shopping.readlines())
#print (shopping_liste)

def normalise(entree) : #(-->str)
    entree = entree.lower() # on ne fait pas de différences entre minuscules et majuscules
    entree = entree.strip()  # supprime les espaces et fin de lignes en début et fin de chaine
    entree = " ".join(entree.split()) # méchant hack pour éviter les espaces multiples restants quelque soit leur nombre
    entree = entree.replace(" : ",":")
    entree = entree.replace(": ",":")
    entree = entree.replace(" :",":")
    return (entree) #(-->str)

def gauche(liste) :
    liste_gauche=[]
    for entree in liste :
        entree=normalise(entree)
        index = entree.find(":")
        if index != -1 :
            partie_gauche = entree[0:index]
            liste_gauche.append(partie_gauche)
    #print (liste_gauche)
    return (liste_gauche)

gauche_shopping_liste=gauche(shopping_liste)
#print (gauche_shopping_liste)

def droite(liste) :
    liste_droite=[]
    for entree in liste :
        entree=normalise(entree)
        index = entree.find(":")
        if index != -1 :
            partie_gauche = entree[0:index]
            partie_droite = int(entree[index+1:len(entree)])
            liste_droite.append(partie_droite)
    #print (liste_droite)
    return (liste_droite)

droite_shopping_liste=droite(shopping_liste)
print (droite_shopping_liste)

def txcroise(liste_g,liste_d) :
    liste_g_clean=[]
    dict_clean={}
    for i in range (1,len(liste_g)) :
        if dict_clean.get(liste_g[i]) is None :
            dict_clean[liste_g[i]] = liste_d[i] 
        else :
            dict_clean[liste_g[i]] = liste_d[i]+dict_clean.get(liste_g[i])

            #print (dict_clean)
    #print (dict_clean)
    return (dict_clean)

dict_gauchedroite=txcroise(gauche_shopping_liste,droite_shopping_liste)
print (dict_gauchedroite)


Sans_doublons = (dict_gauchedroite)


Liste_sans_doublons = open(FILE_PATH+"liste_sans_doublons.txt","w")
Liste_sans_doublons.write(f"{Sans_doublons}\n")
Liste_sans_doublons.close()