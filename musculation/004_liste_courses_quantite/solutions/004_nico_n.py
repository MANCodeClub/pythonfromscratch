shopping_file = open("./liste_avec_doublons.txt","r")

def normalise(item):
    """ prend une str en entrée et retourne une str normalisé """
    item = item.lower() # on ne fait pas de différences entre minuscules et majuscules
    item = item.strip()  # supprime les espaces et fin de lignes en début et fin de chaine
    item = " ".join(item.split()) # méchant hack pour éviter les espaces multiples restants quelque soit leur nombre
    return item

""" Contrairement à l'exercice 003 je traite le fichier ligne par ligne.
On pourrait faire attention que la lecture des lignes se fasse de manière indépendante du stockage dans un fichier.
Evidemment dans notre exercice ce serait un peu exagéré.
Même quand on connait les bonnes pratiques il faut les mettre en oeuvre quand elles se justifient."""

shopping_dict = {} # dans ce dictionnaire l'étiquette sera le nom de l'item à acheter et la valeur sera la quantité.
for line in shopping_file:
    if ":" not in line:
        # on ne conserve pas les lignes dans séparateurs:
        continue
    fields = line.split(":")
    item_name = normalise(fields[0])
    item_number = int(fields[1]) # si ce n'est pas un entier ça plante (avec une exception). Ici je l'accepte...
    shopping_dict[item_name] = shopping_dict.get(item_name, 0) + item_number # si l'item n'est pas déjà dans le dict on initialise sa valeur à 0



clean_shopping_file = open("./liste_sans_doublons.txt","w")
for (item_name, item_number) in shopping_dict.items():
    clean_shopping_file.write(f"{item_name} : {item_number}\n")
