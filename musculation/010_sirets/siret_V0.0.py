import requests
import datetime
import csv
import json
import base64

proxies = {
        "http": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
        "https": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080"
        }

cle = '3FH1jzDdxIg_S0_7NcdIZAZBaoIa'
secret = 'll0htvhgkItaFQjy6vVhrfRcBqIa'

auth = (base64.b64encode(b'3FH1jzDdxIg_S0_7NcdIZAZBaoIa:ll0htvhgkItaFQjy6vVhrfRcBqIa'))
auth = (auth.decode("utf-8"))
auth = f"Basic {auth}"
headers = {"Authorization": auth}

#print (headers)

data = {'grant_type': 'client_credentials'}

token = requests.post(url = 'https://api.insee.fr/token', headers = headers, proxies=proxies, data=data, verify=False)

access_token = json.loads(token.text)
access_token = (access_token.get('access_token'))
#print (f"acces_token = {access_token}")

# en cas de VPN ou de lancement sur site

FILE_PATH="C:/Mes_Auto_Formations/Python"

#print(f"{FILE_PATH}/SIRET_A_Controler.txt")

fichier_RESULTAT = open(f"{FILE_PATH}/fichier_RESULTAT.txt","w")


def Verif(fichier):
    siret_a_controler = open(f"{FILE_PATH}/{fichier}","r",encoding='utf-8')
    lecteur = csv.reader(siret_a_controler, delimiter="|", quotechar='"')
    next(lecteur)
    # on lit la première ligne avec le noms des colonnes pour la passer 
    newrow=[[],[],[],[]]
    for row in lecteur :
        #print (row)
        newrow[0].append(row[0])
        newrow[1].append(row[1])
        newrow[2].append(row[2])
        newrow[3].append(row[3])
    for SIRET_Com in newrow[2] : # Pour chaque SIRET du fichier,
        #SIRET=SIRET.strip()
        fichier_RESULTAT = open(f"{FILE_PATH}/fichier_RESULTAT.txt","a")
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        authorization=(f"Bearer {access_token}")
        #print(f"Authorization = {authorization}")
        headers={"Authorization": authorization}
        #print(f"headers = {headers}")
        url=(f"https://api.insee.fr/entreprises/sirene/V3/siret/{SIRET_Com}?date={date}") # je contruis l'URL correspondante avec en complément la date du jour
        #print (url)
        reponse = requests.get(url, headers=headers, proxies=proxies)
        #print (SIRET_Com)
        #print (reponse.status_code)
        while reponse.status_code in (429,503) : # Tant que la réponse est de type (erreur interne du serveur ou erreur liée à une trop forte sollicitation du serveur),
            reponse = requests.get(url, headers=headers) # je relance ma requête
        
        status_code = reponse.status_code
        if status_code == 200 :
            reponse = reponse.json()
            dateDebut = (reponse['etablissement']['periodesEtablissement'][0]['dateDebut'])
            dateFin = (reponse['etablissement']['periodesEtablissement'][0]['dateFin'])
            etablissment = (reponse['etablissement']['uniteLegale']['denominationUniteLegale'])
            #print (reponse[])
            fichier_RESULTAT.write(f"{SIRET_Com};") # j'écris le SIRET et le code erreur
            fichier_RESULTAT.write(f"{status_code};") # j'écris le SIRET et le code erreur
            fichier_RESULTAT.write(f"{etablissment};") # j'écris le SIRET et le code erreur
            fichier_RESULTAT.write(f"{dateDebut};") # j'écris le SIRET et le code erreur
            fichier_RESULTAT.write(f"{dateFin}\n") # j'écris le SIRET et le code erreur
            fichier_RESULTAT.close()
        else :
            fichier_RESULTAT.write(f"{status_code}\n") # j'écris le SIRET et le code erreur

Verif("SIRET_A_Controler.txt")
