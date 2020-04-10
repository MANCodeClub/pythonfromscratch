def is_shifted(s1, s2):
    """ Cette fonction retourne True si la chaine s2 est égale à la chaine s1 décalé d'un caractère vers la droite
        Elle retourne False sinon.
        Ex: s1 = "azerty", s2="zertya" => True
            s1 = "azerty", s2="azert" => False """
    # NICO M je pense que j'aurais pu introduire une exception pour la chaîne vide
    # NICO V Dans les cas où ça vaut le coup il faudrait traiter tous les contrôles sur les arguments avant tout:
    #   Ici: est-ce que l'un des arguments n'est pas un str?
    # Mais ce n'est pas le but de l'exercice et la fonction de test ne vérifie pas les cas d'argument anormaux.
    # D'ailleurs à l'usage c'est peut-être un test qui sera ajouté si on se rend compte que ça peut réellement arriver.
    if (s1[-1:]+s1[:-1] == s2) and ((s1 != "") or (s2 != "")) : 
        result = True
    else :
        result = False
    return result