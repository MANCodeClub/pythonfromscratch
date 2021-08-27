FILE_PATH="D:/Mes_Etudes/GitMAN_Kraken/pythonfromscratch/musculation/006_insee/"
file_commune=open(FILE_PATH+"communes.csv","r")
file_dep=open(FILE_PATH+"departement.txt","r")

def normalise(item): # On reconnait que ce n'est pas de moi...
    """ prend une str en entrée et retourne une str normalisé """
    #item = item.lower() # on ne fait pas de différences entre minuscules et majuscules
    item = item.strip()  # supprime les espaces et fin de lignes en début et fin de chaine
    item = " ".join(item.split()) # méchant hack pour éviter les espaces multiples restants quelque soit leur nombre
    return item


dep_liste=[[],[],[]] # Je crée une liste (dans le mauvais sens) des départements
for dep in file_dep :
    fields = dep.split(" - ")
    #print (fields)
    dep_liste[0].append(fields[0])#clef de jointure
    dep_liste[1].append(normalise(fields[1]))#nom du département
    dep_liste[2].append(normalise(fields[2]))#nom du chef lieu de département


commune_liste=[[],[],[],[],[]] # Je crée une liste (dans le mauvais sens) des communes
for commune in file_commune :
    fields = commune.split(";")
    if fields[0][0:2] == '2A' :# je traite le cas corse d'entrée car 2A n'est pas un entier
        commune_liste[0].append((fields[0])[0:2])
    elif int(fields[0][0:2]) <= 95 :# les départements métropolotains sont codés sur 2 caractères (clef de jointure)
        commune_liste[0].append((fields[0])[0:2])
    elif int(fields[0][0:2]) > 95 : # les dom sont codés sur 3 caractères (clef de jointure)
        commune_liste[0].append((fields[0])[0:3])
    commune_liste[1].append(normalise(fields[0]))
    commune_liste[2].append(normalise(fields[1]))


for insee in commune_liste[0] : # Je relie mes listes ; l'oblectif de ces 2 boucles imbriquées est de ramener dans la liste "commune_liste" les éléments liés aux départements en utilisant la cléf de jointure (numéro de département)
    if insee[0:2] == '2A' : # je traite la difficulté des départements codés sur 2 / 3 caractères
        key = insee[0:2]    
    elif int(insee[0:2]) <= 95 :
        key = insee[0:2]
    elif int(insee[0:2]) > 95 :
        key = insee[0:3]
    #print (key)
    for dep in dep_liste[0] :
        index=dep_liste[0].index(dep)
        nom_dep = dep_liste[1][index]
        chef_lieu = dep_liste[2][index]
        #print (nom_dep)
        #print (chef_lieu)
        if dep == key :
            #print (nom_dep)
            #print (chef_lieu)
            commune_liste[3].append(nom_dep)
            commune_liste[4].append(chef_lieu)

# A ce moment là, je suis convaincu qu'il fallait créer la liste ("dans l'autre sens") pour pouvoir trier par la suite...
# J'ai essayé mais je n'y suis pas parvenu donc je transpose ma liste... je sais c'est très nul!

transpose_liste=[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]],[[]]# Ca aussi, c'est très nul. J'ai tenté un []*16 sans succès
for n in range (0,len(commune_liste[0])) :
    transpose_liste[n].insert(0,commune_liste[0][n])
    transpose_liste[n].insert(1,commune_liste[1][n])
    transpose_liste[n].insert(2,commune_liste[2][n])
    transpose_liste[n].insert(3,commune_liste[3][n])
    transpose_liste[n].insert(4,commune_liste[4][n])


transpose_liste_tri=(sorted(transpose_liste, key = lambda v: v[1]))
#print(transpose_liste_tri)

# J'écris mon fichier avec les noms de départements et de leurs préfectures
file_resultat=open(FILE_PATH+"communes_resultat.txt","w")
for n in range (0,len(commune_liste[0])) :
    file_resultat.write(f"{transpose_liste_tri[n][0]}|{transpose_liste_tri[n][1]}|{transpose_liste_tri[n][2]}|{transpose_liste_tri[n][3]}|{transpose_liste_tri[n][4]}\n")
