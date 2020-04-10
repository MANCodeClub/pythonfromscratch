""" NVI : Il y a souvent des cafouillages de convention entre dev sur les termes path et dir.
Pour ma part je me tiens à la convention suivante:
filePath = fileDir + / + fileName
ou
file_path = file_dir + / + file_name
"""

FILE_PATH="../"
Liste = open(FILE_PATH+"liste_avec_doublons.txt","r")
""" Tu ne pouvais pas le savoir mais on fait abituellement commencer les noms de variables par des minuscules
On préfère garder les majuscule en début de mot pour les noms de classes.
Et puis tout en majuscule pour les constantes.
"""

Ligne_Liste=(Liste.readlines())
Mot_Liste=[]

for mot in Ligne_Liste :
    mot = mot.strip() # pour épurer les fantaisies syntaxiques
    mot = mot.lower() # pour épurer les fantaisies syntaxiques
    # NVI: je ne pense pas que ce ne serait pas suffisant si j'avais mis 3 espaces consécutifs
    mot = mot.replace("  "," ") # pour épurer les fantaisies syntaxiques
    Mot_Liste.append(mot) # pour génerer une liste en prévision du travail de suppression des doublons

""" J'espérais que vous fassiez ce genre d'algo :-) 
Par contre c'est quand même un peut trop maladroit.
Plutôt que je changer les valeurs par Boublon puis de les supprimer il aurait été plus simple de créer une nouvelle liste vide et de n'y mettre que les nouveaux mots:
clean_list = []
for item in Mot_Liste:
    if item not in clean_list:
        clean_list.append(item)
"""
#print (Mot_Liste)
for n in range (0,len(Mot_Liste)) : # boucle imbriquée
    for i in range (n+1,len(Mot_Liste)) : # pour le premier terme de ma liste, je verifie que les termes suivants ne portent pas le même nom
        if Mot_Liste[n] == Mot_Liste[i] : # si c'est le cas, je renomme le terme redondant en "doublons" / je ne peux pas le supprimer direct car le nombre de terme de ma liste serait différent de celui de départ
            Mot_Liste[i]="Doublons"
    n=n+1 # et je repète cette boucle pour le 2ème terme... jusqu'à avoir tester toute la liste
    
while "Doublons" in Mot_Liste: # pour supprimer les entrées "doublons" (et les lignes vides >> ça, j'aurai dû le faire dès le début mais je ne connais pas la fonction)
    del Mot_Liste[Mot_Liste.index("Doublons")]
while "" in Mot_Liste:
    del Mot_Liste[Mot_Liste.index("")]

print (Mot_Liste)

Liste_sans_doublons = open(FILE_PATH+"liste_sans_doublons.txt","w")
for n in range (0,len(Mot_Liste)) :
    Liste_sans_doublons.write(f"{Mot_Liste[n]}\n") # pour obtenir une liste verticale
Liste_sans_doublons.close()