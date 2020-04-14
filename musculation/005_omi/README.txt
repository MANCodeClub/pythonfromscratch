Les navire de commerces possèdent tous un numéro d'immatriculation international dit numéro OMI (ou IMO number).
Ce numéro respecte plusieurs règles:
1- Il est constitué de 7 chiffres
2- il ne commence pas par 0
3- Le dernier chiffre doit être le chiffre des unité de la somme des six premiers multipliés par (8 - leur position)

Zavez rien compris? On va faire un exemple:

Par exemple:
9074729

On fait le calcul avec les 6 premiers chiffres:
(9×7) + (0×6) + (7×5) + (4×4) + (7×3) + (2×2) = 139

le résultat se termine par 8 donc le dernier chiffre du numéro doit être un 9

Second exemple:
1111117
1*7 + 1*6 + 1*5 + 1*4 + 1*3 + 1*2 = 27
Donc le dernier chiffre doit bien être un 7

Nous devons écrire une fonction checkIMONbr(numero) qui va contrôler que notre numéro est correct.
Evidemment le dev de chez Capgémini a réussi à se planter. 
Mais c'est parce qu'il n'avait pas de test unitaire, ce qui n'est pas votre cas!

Quand ce sera bon vous coderez checkIMOField() qui fait le même travail mais l'argument 
de la fonction est une chaine de caractère qui vient d'une saisie manuelle et rien ne nous 
garantie qu'elle n'est pas fantaisiste. Les gens tapent vraiment n'importe quoi.

Pour tester votre code taper simplement 
python test.py