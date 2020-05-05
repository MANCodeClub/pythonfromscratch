"""
Ce programme doit deviner le nombre auquel vous pensez.

Vous choisissez un nombre en 1 et 100.
Vous lancer le programme.
Il vous propose des nombres et vous lui répondez si votre nombre est plus grand (+), plus petit (-) ou s'il a gagné (=).

Votre programme doit trouver la solution le plus rapidement possible par dichotomie.
C'est à dire qu'il propose toujours un nombre a peu près au milieu de l'intervalle possible.

exemple:
50? (milieu de l'intervalle 1-100)
-
25? (milieu de l'intervalle 1-49)
- 
12? +
18? -
15? -
13? +
14? =
Super! J'ai gagné!


"""
import random
print ("Choisissez un nombre compris entre 1 et 100")
print ("Je vais le deviner!")
mini = 0
maxi = 100
nombrecherche = int(random.random()*100) # le nombre de départ est choisi aléatoirement ; c'est plus rigolo que de commencer par 50
print (f"le nombre recherché est {nombrecherche} ?")
reponse = input ("tapez =, +, ou -")
while reponse != "=" : # tant que la réponse n'est pas correcte, j'execute les instructions ci-dessous :
    if reponse == "+" : # le nombre proposé est incorrect et (aussi) trop bas
        mini = nombrecherche # le mini passe de 0 (ou de sa dernière valeur) au dernier nombre proposé par l'ordinateur
        nombrecherche = int ((mini+maxi)/2) # le nombre proposé est à mi chemin entre ce mini et le maxi (100 ou sa dernière valeur)
        print (f"le nombre recherché est {nombrecherche} ?")
        reponse = input ("tapez =, +, ou -") # on repose la question
    if reponse == "-" : # le nombre proposé est incorrect et (aussi) trop haut
        maxi = nombrecherche # le maxi passe de 100 (ou de sa dernière valeur) au dernier nombre proposé par l'ordinateur
        nombrecherche = int ((mini+maxi)/2) # le nombre proposé est à mi chemin entre ce maxi et le mini
        print (f"le nombre recherché est {nombrecherche} ?")
        reponse = input ("tapez =, +, ou -") # on repose la question
print ("j'ai trouvé!")
# il y a un bais // les nombres 1 et 100 sont inatteignables en raison de la troncature effectuée sur la moyenne (un arrondi aurait permis d'atteindre ces valeurs)
# j'ai des lignes "doublons" qui auraient sans doute pu être "factorisées" en construisant une boucle plus astucieuse... je vais aller voir la solution!