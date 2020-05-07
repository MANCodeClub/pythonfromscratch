import requests
import datetime

proxies = {
        "http": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
        "https": "https://pfrie-std.proxy.e2.rie.gouv.fr:8080"
    }
# en cas de VPN ou de lancement sur site

FILE_PATH="D:/Mes_Etudes/Python/"
token = "4f6040ec-6cd3-3681-915c-17642d129cee" # Renseigner le token préalablement récupéré sur le site api.insee.fr


fichier_controle = open(f"{FILE_PATH}SIRET_A_Controler.txt","r")
fichier_SIRET=(fichier_controle.readlines())
for SIRET in fichier_SIRET : # Pour chaque SIRET du fichier,
    SIRET=SIRET.strip()
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    authorization=(f"Bearer {token}")
    print(f"Authorization = {authorization}")
    headers={"Authorization": authorization}
    print(f"headers = {headers}")
    url=(f"https://api.insee.fr/entreprises/sirene/V3/siret/{SIRET}?date={date}") # je contruis l'URL correspondante avec en complément la date du jour
    print (url)
    reponse = requests.get(url, headers=headers)
    print (SIRET)
    print (reponse.status_code)
    while reponse.status_code in (429,503) : # Tant que la réponse est de type (erreur interne du serveur ou erreur liée à une trop forte sollicitation du serveur),
        reponse = requests.get(url, headers=headers) # je relance ma requête
    dict={SIRET:(reponse.status_code)}
    print(dict)
    if reponse.status_code != 200 : # Pour chaque réponse différente de SIRET valide
        fichier_RESULTAT = open(f"{FILE_PATH}fichier_RESULTAT.txt","w")
        fichier_RESULTAT.write(f"{dict}") # j'écris le SIRET et le code erreur
        fichier_RESULTAT.close()
