from lxml import etree
import os
import requests
import datetime
import json



#dictionnaire imbriqué
#PATH = "C:\\_Mes_Etudes\\MCO06_Exploitation\\2016_FEN\\A_Virer\\"

proxies = {
        "http": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080",
        "https": "http://pfrie-std.proxy.e2.rie.gouv.fr:8080"
        }

headers={"Authorization": "Basic M0ZIMWp6RGR4SWdfUzBfN05jZElaQVpCYW9JYTpsbDBodHZoZ2tJdGFGUWp5NnZWaHJmUmNCcUlh"}


data = {'grant_type': 'client_credentials'}

token = requests.post(url = 'https://api.insee.fr/token', headers = headers, proxies=proxies, data=data, verify=False)

access_token = json.loads(token.text)
access_token = (access_token.get('access_token'))
print (access_token)


def REP():
    REP_WINDOWS = input (f"Indiquez le répertoire de stokage des FEN par un copier/coller de l'explorateur windows?")
    REP_NORM = os.path.normpath(REP_WINDOWS)
    global REP_PAR_UNIX
    REP_PAR_UNIX = os.path.dirname(REP_NORM)
    os.makedirs(REP_PAR_UNIX+"\\OUTPUT\\", exist_ok=True)
    print (REP_WINDOWS)
    print (REP_PAR_UNIX)
    return  REP_PAR_UNIX


export_FEN = open(REP()+"\\export_FEN.txt","w",encoding='utf-8')#j'ouvre en écriture un fichier pour récupérer les titres avec le nom DDT comme redevable



# en cas de VPN ou de lancement sur site
def code_SIRET(SIRET):    
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    authorization=(f"Bearer {access_token}")
    champs = "denominationUniteLegale"
    masquerValeursNulles = True
    headers={"Authorization": authorization}
    print(f"Authorization = {authorization}")
    print(f"headers = {headers}")
    url=(f"https://api.insee.fr/entreprises/sirene/V3/siret/{SIRET}?date={date}&champs={champs}&masquerValeursNulles={masquerValeursNulles}") # je contruis l'URL correspondante avec en complément la date du jour
    print (url)
    reponse = requests.get(url, headers=headers, proxies=proxies)
    print (SIRET)
    print (reponse.text)
    while reponse.status_code in (429,503) : # Tant que la réponse est de type (erreur interne du serveur ou erreur liée à une trop forte sollicitation du serveur),
        reponse = requests.get(url, headers=headers, proxies=proxies) # je relance ma requête
    #etablissement={SIRET:['Etablissement'][0]['uniteLegale'][denominationUniteLegale]}
    if reponse.status_code == 200 :
        etablissement = reponse.json()#[etablissement]
    #etablissement = json.JSONDecoder().decode()
        for key, value in etablissement.items():
            print(key, ":", value)
        print (etablissement)
        etablissement = etablissement["etablissement"]["uniteLegale"]["denominationUniteLegale"]
        print (type (etablissement))
        print (etablissement)
    else :
        etablissement = (f"ERREUR = {reponse.status_code}")
    #etablissement = 'MN'
    return etablissement
    #etablissement = 'NON_EXECUTE'
    #return etablissement

def code_SIRET_Light(SIRET):    
    etablissement = SIRET
    return etablissement


def apure(file):
    n = 0
    FEN_Source = open(REP_PAR_UNIX+"\\INPUT\\"+file,"r",encoding="ISO-8859-15")
    FEN_XML = open(REP_PAR_UNIX+"\\OUTPUT\\"+file+".xml","w",encoding="utf-8")
    for line in FEN_Source:
        #print(line)
        n = n + 1
        if n == 1 :
            pass
        elif n == 2 :
            FEN_XML.write("<FEN0052A>"+"\n")
        else :
            FEN_XML.writelines(line)
    FEN_XML.close()
    return FEN_XML


def parse(fic):


    Dict_Imbrique_Deb = {'REFADS':{'DESIGNATION':'ADR_RUE'}}    
    Dict_Imbrique_FA  = {'REFADS':{'TYPE_TITRE':'NUM_FACT'}}
    Dict_Imbrique_Com = {'REFADS':{'PART_COM':'CODE_SIRET'}}
    Dict_Imbrique_Dep = {'REFADS':{'PART_DEP':'CODE_SIRET'}}
    Dict_Imbrique_Reg = {'REFADS':{'PART_REG':'CODE_SIRET'}}
    Dict_Imbrique_RAP = {'REFADS':{'PART_RAP':'CODE_SIRET'}}
    Dict_Imbrique_CR = {'REFADS':{'CR':'CODE_SIRET'}}



    #Tx_Avoir = [['REF_ADS'],['TYPE_TITRE'],['NUM_FACT']]#j'initie la premiere ligne d'un tableau de x éléments
    #Tx_Siret = [['REF_ADS'],['TYPE_TITRE'],['NUM_FACT'],[Dict_Com],[Dict_Dep],[Dict_Reg],[Dict_RAP],['FIC']]#j'initie la premiere ligne d'un tableau de x éléments

    tree = etree.parse(fic)
    #root_fen = tree.getroot()
    #print (tree)
    Ligne_Deb    =  tree.xpath("/FEN0052A/FACTURE/OCCASIONNEL")
    Ligne_Poste  =  tree.xpath("/FEN0052A/FACTURE/LIGNE_POSTE")
    Ligne_Entete =  tree.xpath("/FEN0052A/FACTURE/ENTETE")

    #print (type(Ligne_Deb))
    #print (type(Ligne_Poste))
    #print (type(Ligne_Entete))

    n = 0
    while n < (len(Ligne_Deb)) :
        #print (Ligne_Deb[n][6].text)
        Dict_Imbrique_Deb[(Ligne_Deb[n][2]).text]={((Ligne_Deb[n][5]).text):(Ligne_Deb[n][10]).text}
        n = n + 1

    n = 0
    while n < (len(Ligne_Poste)) :
        #print (((Ligne_Poste[n][4]).text)[0:6])
        if ((Ligne_Poste[n][4]).text)[0:6] == 'Part c':
            Dict_Imbrique_Com[(Ligne_Poste[n][2]).text]={((Ligne_Poste[n][31]).text):code_SIRET_Light((Ligne_Poste[n][31]).text)}
            n = n + 1
        else :
            n = n + 1

    n = 0
    while n < (len(Ligne_Poste)) :
        #print (((Ligne_Poste[n][4]).text)[0:6])
        if ((Ligne_Poste[n][4]).text)[0:6] == 'Part d':
            Dict_Imbrique_Dep[(Ligne_Poste[n][2]).text]={((Ligne_Poste[n][31]).text):code_SIRET_Light((Ligne_Poste[n][31]).text)}
            n = n + 1
        else :
            n = n + 1

    n = 0
    while n < (len(Ligne_Poste)) :
        #print (((Ligne_Poste[n][4]).text)[0:6])
        if ((Ligne_Poste[n][4]).text)[0:6] == 'Part r':
            Dict_Imbrique_Reg[(Ligne_Poste[n][2]).text]={((Ligne_Poste[n][31]).text):code_SIRET_Light((Ligne_Poste[n][31]).text)}
            n = n + 1
        else :
            n = n + 1

    n = 0
    while n < (len(Ligne_Poste)) :
        #print (((Ligne_Poste[n][4]).text)[0:6])
        if ((Ligne_Poste[n][4]).text)[0:6] == 'Redeva':
            Dict_Imbrique_RAP[(Ligne_Poste[n][2]).text]={'parametrage':((Ligne_Poste[n][8]).text)}
            n = n + 1
        else :
            n = n + 1
            
    n = 0
    while n < (len(Ligne_Poste)) :
        #print (((Ligne_Poste[n][4]).text)[0:6])
        if ((Ligne_Poste[n][3]).text) == '001':
            Dict_Imbrique_CR[(Ligne_Poste[n][2]).text]={((Ligne_Poste[n][16]).text):code_SIRET_Light((Ligne_Poste[n][16]).text)}
            n = n + 1
        else :
            n = n + 1

    n = 0
    while n < (len(Ligne_Entete)) :
        #print ((Ligne_Entete[n][0]).text)
        Dict_Imbrique_FA[((Ligne_Entete[n][2]).text)] = {(Ligne_Entete[n][0]).text:(Ligne_Entete[n][10]).text}
        n = n + 1

    #print (f"Dict_Imbrique_Deb = {Dict_Imbrique_Deb}")
    #print (f"Dict_Imbrique_Com = {Dict_Imbrique_Com}")
    #print (f"Dict_Imbrique_Dep = {Dict_Imbrique_Dep}")
    #print (f"Dict_Imbrique_Reg = {Dict_Imbrique_Reg}")
    #print (f"Dict_Imbrique_RAP = {Dict_Imbrique_RAP}")
    #print (f"Dict_Imbrique_FA = {Dict_Imbrique_FA}")



    o = 0

    #TX_Final = ['REF_ADS'],['TYPE_TITRE'],['NUM_FACT'],['Dict_Com'],['Dict_Dep'],['Dict_Reg'],['Dict_RAP'],['FIC']
    TX_Final = [],[],[],[],[],[],[],[]#["Ref_ADS"],["Débiteur"],["Avoir-Facture"],["Part_Com"],["Part_Dep"],["Part_Reg"],["Fic"]
    for key, value in Dict_Imbrique_FA.items():
        #print (f"key={key}")
        #REF_ADS = key
        #print (f"values={value}")
        #print (Dict_Imbrique_FA.get(key, "Par_Defaut"))
        TX_Final[0].append(key)
        TX_Final[1].append(Dict_Imbrique_Deb.get(key))
        TX_Final[2].append(Dict_Imbrique_FA.get(key, {key:"Pas de facture de Ref"}))
        TX_Final[3].append(Dict_Imbrique_Com.get(key,{key:"Pas de part Com"}))
        TX_Final[4].append(Dict_Imbrique_Dep.get(key,{key:"Pas de part Dep"}))
        TX_Final[5].append(Dict_Imbrique_Reg.get(key,{key:"Pas de part Reg"}))
        TX_Final[6].append(Dict_Imbrique_CR.get(key,{key:"IMP"}))

    print (TX_Final)
    #export_FEN = open("export_FEN.txt","a",encoding='utf-8')#j'ouvre en écriture un fichier pour récupérer les titres avec le nom DDT comme redevable
    while o < len((TX_Final)[0]):
        for designation in TX_Final[0]:
            #print (designation)
            if (designation.upper().find(Dossier_Find)) != -1 :
                export_FEN.write(f"{TX_Final[0][o]};") #sur la ligne o, j'écris REF_ADS,
                export_FEN.write(f"{TX_Final[1][o]};") #sur la ligne o, j'écris REF_ADS,
                export_FEN.write(f"{TX_Final[2][o]};") #--DESIGNATION,
                for SIRET01,SIRET02 in TX_Final[3][o].items():
                    print (SIRET02)
                    if 'Pas' in SIRET02 :
                        export_FEN.write(f"-;")
                        export_FEN.write(f"{SIRET02};")
                    else :
                        export_FEN.write(f"{SIRET02};")
                        export_FEN.write(f"{code_SIRET(SIRET02)};")
                for SIRET01,SIRET02 in TX_Final[4][o].items():
                    print (SIRET02)
                    if 'Pas' in SIRET02 :
                        export_FEN.write(f"-;")
                        export_FEN.write(f"{SIRET02};")
                    else :
                        export_FEN.write(f"{SIRET02};")
                        export_FEN.write(f"{code_SIRET(SIRET02)};")
                for SIRET01,SIRET02 in TX_Final[5][o].items():
                    print (SIRET02)
                    if 'Pas' in SIRET02 :
                        export_FEN.write(f"-;")
                        export_FEN.write(f"{SIRET02};")
                    else :
                        export_FEN.write(f"{SIRET02};")
                        export_FEN.write(f"{code_SIRET(SIRET02)};")
                for SIRET01,SIRET02 in TX_Final[6][o].items():
                    print (SIRET02)
                    if 'IMP' in SIRET02 :
                        export_FEN.write(f"-;")
                        export_FEN.write(f"{SIRET02};")
                    else :
                        export_FEN.write(f"{SIRET02};")
                        export_FEN.write(f"{code_SIRET(SIRET02)};")               
                export_FEN.write(f"{fic}\n")
                o=o+1
            else :
                o=o+1
    #print (TX_Final)
    return TX_Final



for fichier in os.listdir(REP_PAR_UNIX+"\\INPUT\\"):
    apure(fichier)

global Dossier_Find
Dossier_Find = input (f"Indiquez les premiers caractères du titre à analyser?")


for fichier in os.listdir(REP_PAR_UNIX+"\\OUTPUT\\"):
    parse(REP_PAR_UNIX+"\\OUTPUT\\"+fichier)
