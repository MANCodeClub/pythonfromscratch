def is_shifted(s1, s2):

    """
    Cette fonction retourne le nombre de caractère de décalage vers la droite de la seconde chaine par rapport à la première
        Elle retourne -1 si les chaines ne sont pas comparables.
        Ex: s1 = "azerty", s2="zertya" => 1
            s1 = "azerty", s2="azert" => -1
    """

    dict1 = {} # j'initie un dictionnaire
    dict2 = {} # j'initie un dictionnaire
    decalage = 0 # j'initie une variable de type "integer" pour stocker le décalage

    for letter in s1 :
        dict1[letter] = s1.index(letter) # le dictionnaire s1 est alimenté {'a': 0, 'z': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5}
    for letter in s2 :
        dict2[letter] = s2.index(letter) # le dictionnaire s2 est alimenté {'z': 0, 'e': 1, 'r': 2, 't': 3, 'y': 4, 'a': 5}
    for letter in dict1.keys() : # pour chaque lettre de azerty, je calcule la différence des clefs correspondantes entre les dictionnaires, j'obtiens pour chaque lettre un nombre identique modulo la longueur de chaîne
        if dict2[letter] < dict1[letter] :
            decalage = dict2[letter] - dict1[letter] + len (s1)
        else :
            decalage = dict2[letter] - dict1[letter]

    if len (s2) != len (s1) : ###Exception 1  : les chaines présentent un nombre total de caractères différent.
        decalage = -1
    
    for letter in s1 :
        if (s2.find(letter)) == -1 : ###Exception 2 : au moins un caractère d'une chaine est introuvable dans l'autre.
            decalage = -1
    
    return decalage
