Contrôle des SIRETS :
Besoin minimal :
A partir d'un fichier txt qui prend la forme d'une suite de SIRET (issus de la BDD d'ADS),
j'utilise le service api.insee.fr pour les contrôler un à un.
A chaque fois que la réponse fournie par l'API indique que le siret est erroné, j'écris le SIRET invalide dans un fichier.
Au final, j'obtiens la liste des SIRET invalides à partir d'une liste d'entrée
