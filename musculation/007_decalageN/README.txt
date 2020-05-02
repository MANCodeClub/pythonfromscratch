Dans l'exercice 001 il fallait déterminer si une chaine était décalé d'un caractère par rapport à une autre.
Ici on va chercher si deux chaines sont décalées l'une par rapport à l'autre et retourner le nombre de caractère de décalage.

exemples:
"AZERTY" "YAZERT" => décalage 1
"AZERTY" "TYAZER" => décalage 2
"AZERTY" "ZERTYA" => décalage 5

Le décalage est déplacement de la seconde chaine par rapport à la première vers la droite.

S'il n'est pas possible d'obtenir la nouvelle chaine par décalage de la première on retourne -1.

exemple:
"AZERTY" "UIOP" => décalage -1 

