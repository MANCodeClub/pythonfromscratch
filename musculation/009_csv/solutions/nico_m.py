"""
Votre mission sera donc d'utiliser le module csv pour lire un export CSV de mantis et 
de générer un nouveau csv dont le format sera le suivant:

0 Identifiant,
1 Résumé,
2 Statut,
3 Version ciblée,
4 Version du produit

<numéro du ticket> 0
<statut> 2
<version_cible> 3
<titre du ticket> 1
"""

import csv
mantis = open("mantis.csv","r")
lecteur = csv.reader(mantis, delimiter=",", quotechar='"')
# on lit la première ligne avec le noms des colonnes pour la passer 
next(lecteur)

esc_file = open("mantis_output.csv","w")
ecrivain = csv.writer(esc_file, delimiter=" ", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
newrow=[["numéro du ticket"],["statut"],["version_cible"],["titre du ticket"]]

for row in lecteur :
    newrow[0].append(row[0])
    newrow[1].append(row[2])
    newrow[2].append(row[3])
    newrow[3].append(row[1])
print (newrow)

for n in range (0,len (newrow[0])) :
    ecrivain.writerow((newrow[0][n],newrow[1][n],newrow[2][n],newrow[3][n]))

# Je vais voir la solution !