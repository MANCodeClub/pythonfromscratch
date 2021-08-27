import requests
import csv

proxies = {
    "http" : "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
    "https": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
}


#on souhaite avoir une réponse en json => on l'indique dans les entêtes


code_postaux_a_verifier = open("a_verifier.csv","r",encoding='utf-8')

a_verifier = csv.reader(code_postaux_a_verifier, delimiter="|", quotechar='"')
next (a_verifier)
#on lit la première ligne avec le noms des colonnes pour la passer
code_postal_new = [['dossier_id'],['numero'],['td'],['code_postal'],['commune']]#j'initie la premiere ligne d'un tableau de 5 éléments
for row in a_verifier : #pour chaque ligne du fichier
    code_postal_new[0].append(row[0])#j'ajoute en fin du 1er élément  (dossier_id)          de la liste la 1ere colonne de la ligne n
    code_postal_new[1].append(row[1])#j'ajoute en fin du 2nd élément  (numero_dossier)      de la liste la 2nde colonne de la ligne n
    code_postal_new[2].append(row[2])#j'ajoute en fin du 3ème élément (td)                  de la liste la 3ème colonne de la ligne n
    code_postal_new[3].append(row[3])#j'ajoute en fin du 3ème élément (adr_td_code)         de la liste la 4ème colonne de la ligne n
    code_postal_new[4].append(row[4])#j'ajoute en fin du 4ème élément (adr_td_localitede)   de la liste la 5ème colonne de la ligne n
#print (code_postal_new)

code_postaux_verifie = open("verifie.txt","w",encoding='utf-8')

headers = {"Accept": "application/json"}

url_api_code_postal = "https://apicarto.ign.fr/api/codes-postaux/communes/"

n=0

#requête recherche de mouvements
#response = requests.get(f"{url_api_code_postal+code_postal}",headers=headers)
for code in code_postal_new[3] : #pour chaque élément du second bloc (chaque code postal) de liste code_postal_new
    url_appel = url_api_code_postal + code
    reponse = requests.get(url_appel, proxies=proxies , headers=headers)#Avec Proxy en VPN
    #reponse = requests.get(url_appel, headers=headers)# Hors VPN
    code_postaux_verifie.write(f"{code_postal_new[0][n]};") #sur la ligne n, je (ré)écris le dossier_id,
    code_postaux_verifie.write(f"{code_postal_new[1][n]};") #--le numéro de dossier,
    #code_postaux_verifie.write(f"{element};")
    code_postaux_verifie.write(f"{code_postal_new[2][n]};") #--l'objet concerné terrain ou demandeur,
    code_postaux_verifie.write(f"{code_postal_new[3][n]};") #--le code postal,
    code_postaux_verifie.write(f"{code_postal_new[4][n]};") #--la commune,
    print (reponse.status_code)
    if reponse.status_code != 200 :#si code postal introuvable
        #print (reponse.status_code)
        #code_postaux_verifie.write(f"{reponse.status_code};")
        code_postaux_verifie.write((f"erreur_suspectée\n")) #--l'erreur puis je change de ligne
        n=n+1    #je compte les tours de boucle
        continue #je reprends la boucle après le test
    rep = reponse.json()
    #print(code_postal_new[3][n])
    dictionnaire={} #j'initie un dictionnaire
    nbre_element = len(rep) #ma réponse est une liste d'élément de type dictionnaire
    o = 0 #compteur d'élémént renvoyé
    for element in rep : #pour chaque élement renvoyé
        dictionnaire=(rep[o]) #je crée un dictionnaire par élément
        print (dictionnaire["nomCommune"])
        if (dictionnaire["nomCommune"]) == code_postal_new[4][n] : #si la valeur de la clé nomCommune (déterminée à partir du code postal au moyen de l'api) correspond à la commune issues de la BDD
            code_postaux_verifie.write((f"OK\n")) #--OK
            break #et je sors de la boucle
        o+=1
        if o == nbre_element : #si j'ai passé tous les élements sans correspondance établie
            code_postaux_verifie.write((f"erreur_suspectée\n")) #--erreur suspectée
        #m=+
    n=n+1


code_postaux_verifie.close
