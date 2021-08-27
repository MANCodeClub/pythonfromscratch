filePath = 'chemin du fichier avec doublons'      #à modifier selon emplacement
listeV0 = open (filePath,'r')                                               #liste avec doublons V0
articles = (listeV0.readlines())                                            
#print(articles) 

nouveau = 'chemin du fichier qui accueillera la nouvelle liste'                         #fichier qui va recevoir la nouvelle liste, à modifier selon emplacement
ecrire = open (nouveau,'w')        


i = 0   # pour lire articles de la liste
liste=[]

for i in range (i,len(articles)):               # pour passer en revue tous les articles de la liste (il n'y a qu'1 art/ ligne)
        
        majusc = articles[i].upper()            # mettre les chaînes de caractères en majuscules 
        #print (majusc)
        sansEsp=majusc.split()                 #suppression espaces multiples
        #print(sansEsp)        
        liste.append(sansEsp)
#print(liste)

liste2 = []
for element in liste:
    if element != [] and element not in liste2: #suppression des lignes vides et suppression des doublons
        liste2.append(element)
#print (liste2)
#print (len(liste2))

motEspace = ''                                  #remettre espace pour les articles composés de plusieurs mots
for elements in liste2:
    z=motEspace = (' '.join(elements))
    ecrire.write(motEspace + ' \n')
    
ecrire.write("C'est bien joli mais il manque le pastis du petit Nico dans cette liste de courses !")


