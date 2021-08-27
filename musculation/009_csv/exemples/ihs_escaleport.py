""" Dans ce script on converti le fichier CSV des navires fourni pas la société IHS en un fichier CSV compatible avec Escaleport.
C'est une version simplifiée d'un script réel pour montrer comment utiliser le module CSV.
"""
import csv

ihs_file = open("ihs_ships.csv","r")
lecteur = csv.reader(ihs_file, delimiter="|", quotechar='"')
# on lit la première ligne avec le noms des colonnes pour la passer 
next(lecteur)

esc_file = open("esc_ships.csv","w")
ecrivain = csv.writer(esc_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

for row in lecteur:
    newrow = row[0:12] + row[13:17]      # suppression du  flagName (colonne 13)
    newrow.append(' '.join(row[17:19]))  # fusion des colonnes NumberOfPropulsionUnits et PropellerType
    newrow += row[19:]                   # on conserve le reste des colonnes
    newrow[8] = ''                       # on vide la colonne 9
    ecrivain.writerow(newrow)