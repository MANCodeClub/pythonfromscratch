IN_FILE_PATH  = "../liste_avec_doublons.txt" # le chemin relatif est portable mais il oblige à lancer le script depuis le répertoire du fichier
""" On peut aussi faire un chemin relatif par rapport au script lui même.
Dans ce cas il peut être lancé de n'importe où mais il faut quand même que le 
fichier soit au bon endroit par rapport au script."""
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_FILE_PATH = f"{SCRIPT_DIR}/../liste_sans_doublons.txt"

""" Dans ma "correction" je sépare bien la lecture et l'écriture des fichiers du travail proprement dit.
Cette habitude permet de tester plus facilement les fonctions dedoublonne et normalise comme on l'a fait dans l'exercice 001.
On pourrait écrire un script de test qui valide ces deux fonctions sans avoir besoin de fichiers.
Elle sont aussi réutilisables si au lieu d'utiliser des fichiers on a une requête http ou une base de donnée...
"""
# acquisition des données
shopping_file = open(IN_FILE_PATH,"r")
shopping_list = shopping_file.readlines()
shopping_file.close()

def normalise(line):
    """ prend une str en entrée et retourne une str normalisé """
    item = line.lower() # on ne fait pas de différences entre minuscules et majuscules
    item = item.strip()  # supprime les espaces et fin de lignes en début et fin de chaine
    item = " ".join(item.split()) # méchant hack pour éviter les espaces multiples restants quelque soit leur nombre
    return item

def dedoublonne(shopping_list):
    """ prend une liste de str en entrée et retourne une set des items normalisés """
    uniq_set = set() # j'avoue je ne vous en ai vraiment pas beaucoup parlé de celui là ;-) mais les sets ça sert à ça aussi.
    for line in shopping_list:
        uniq_set.add(normalise(line))
    return uniq_set

def dedoublonne_sans_set(shopping_list):
    """ retourne une liste sans doublon """
    clean_list = []
    for item in shopping_list:
        item = normalise(item)
        if item not in clean_list:
            clean_list.append(item)
    return clean_list


# enregistrement du résultat
clean_shopping_file = open(OUT_FILE_PATH,"w")
#for item in dedoublonne_sans_set(shopping_list) :
for item in dedoublonne(shopping_list) :
    clean_shopping_file.write(f"{item}\n")
clean_shopping_file.close()