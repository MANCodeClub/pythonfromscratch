import sys

def affiche_drapeau (demi_taille):
    """version de Sandy"""     
    #T=int(input('demi-hauteur T?   ')) > T remplacé par demi_taille 
    larg = demi_taille-1 #largeur dudrapeau

    i=0
    for val in range (0,demi_taille):
        print ('|'+i*'X'+' '+(larg-i)*'X'+' '+(larg-i)*'X'+' '+i*'X'+'|')
        i+=1
        
    lmil = '|'+((2*demi_taille)+1)*' '+'|' #ajout parenthèses sinon erreur qd 0
    print (lmil)    
        
    i=larg
    for val in range (0,demi_taille):
        print ('|'+i*'X'+' '+(larg-i)*'X'+' '+(larg-i)*'X'+' '+i*'X'+'|')
        i-=1       

"""Au démarrage du programme sys.argv est une liste contenant tous les paramètres transmis par la ligne de commande.
argv[0] est le nom du script et on espère avoir le demi-coté dans argv[1]."""
if len(sys.argv) != 2:
    print("Indiquer le demi coté en paramètre:")
    print("Par exemple:")
    print("> python solve.py 5")
    exit(1)
    
demi_taille = int(sys.argv[1])
affiche_drapeau(demi_taille)
