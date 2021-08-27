def dep_from_com(insee):
    """ Retourne le code insee du département à partir du code insee de la commune.
    La seule difficulté se situe dans le traitement des DOM dont le code est sur 
    3 caractères."""
    d_code = insee[:2]
    if d_code in ("97","98"):
        d_code = insee[:3]
    return d_code


deps = {} # dictionnaire pour traduire le code du département par son nom.
# NVI: utilisation de la strucure with pour varier un peu:
# avec with le fichier est automatiquement fermé à la fin du bloc.
# on le rencontre fréquemment dans la nature.
with open("departement.txt", "r") as dep_file:
    for line in dep_file:
        (code, name, pref) = line.split(" - ")
        deps[code] = name

coms = [] #liste des communes. on va y stocker des tuples (insee commune, nom commune, nom département)
with open("communes.csv", "r") as com_file:
    for line in com_file:
        (c_code, c_name) = line.split(";")
        coms.append((c_code, c_name.strip(), deps[dep_from_com(c_code)]))

coms.sort()
for com in coms:
    print(com[0], com[1], com[2], sep="\t")


