import os

def ajoute(stock,legume,quantite): 
    if legume in stock:
        stock[legume] = stock[legume] + quantite
    else:
        stock[legume] = quantite

chemin_list_init = 'C:/Users/sandrine.holub/Documents/recup_git/pythonfromscratch/musculation/004_liste_courses_quantite/liste_avec_doublons_qtt.txt'
chemin_list_fin = 'C:/Users/sandrine.holub/Documents/recup_git/pythonfromscratch/musculation/004_liste_courses_quantite/004_liste_courses_qtt_vf.txt'


liste_intermediaire = []

# à partir du fichier, je lis et travaille sur chaque ligne en vue d'alimenter une liste formatée
with open(chemin_list_init, 'r',encoding='utf-8') as lecture_liste: 
    # Opérations sur le fichier
    for line in lecture_liste:
        if not line.isspace():          #suppression des lignes vides
            line_low = line.lower()
            line_sans_esp = line_low.strip()      #suppression espaces avant/après
            line_sans_esp = line_sans_esp.replace(' :',':')       #suppression espace avant ':'
            line_sans_esp = line_sans_esp.replace('  ',' ')       #suppression doubles espaces            
            line_sans_esp = line_sans_esp.replace('marseille','Marseille')
            line_sans_esp = line_sans_esp.split(':')
            liste_intermediaire.append(line_sans_esp) #liste avec format OK
       
           
print(f'---------------------------LISTE intermédiaire : \n {liste_intermediaire} \n -----------------------------------------------------------')
        
inventaire = {} #dico initié pour faire l'inventaire 
        
i = 0
while i <len(liste_intermediaire):
    print(liste_intermediaire[i])
    if len (liste_intermediaire[i]) == 1:   #pour gérer ligne avec légume sans quantité (donc = 1)
        (liste_intermediaire[i]).append('1')
        ajoute(inventaire,liste_intermediaire[i][0],int(liste_intermediaire[i][1]))
        print(liste_intermediaire[i])    
        i += 1
    else:                                   #pour gérer les légumes avec qtte indiquée
        ajoute(inventaire,liste_intermediaire[i][0],int(liste_intermediaire[i][1]))
        i+=1
        

#print (inventaire)   



#enregistrement du résultat dans un fichier
fichier_RESULTAT = open(f'{chemin_list_fin}','w',encoding='utf-8')


    
for article, qtte in inventaire.items() :
    print (f'{article} : {qtte}')
    fichier_RESULTAT.write(f'{article} : {qtte} \n')




#os.system('pause')
