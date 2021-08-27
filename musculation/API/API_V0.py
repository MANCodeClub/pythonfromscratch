from fastapi import FastAPI
import psycopg2
import sshtunnel
from sshtunnel import SSHTunnelForwarder

app = FastAPI()
@app.get("/{insee}")
def Commune(insee):
    # Tunnel Config
    SSH_HOST = "vm-doo-pg-rec-35*"
    SSH_USER = "*"
    SSH_PASS = "@****07"

    tunnel = sshtunnel.SSHTunnelForwarder(
        (SSH_HOST,22),
        ssh_username = SSH_USER,
        ssh_password = SSH_PASS,
        remote_bind_address=("vm-doo-pg-rec-35.recette.doo.cp2i.e2.rie.gouv.fr", 5432),
        local_bind_address=("localhost",6543)
    )
    tunnel.start()
    print(tunnel.local_bind_port)
    print(tunnel.local_bind_host)
    port = (tunnel.local_bind_port)
    try:
        conn = psycopg2.connect(
            user = "ads3",
            password = "K2******",
            host=tunnel.local_bind_host,
            port=tunnel.local_bind_port,
            database = "ads3"
        )
        cur = conn.cursor()

        # Afficher la version de PostgreSQL 
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("Version : ", version,"\n")


        
        cur.execute(f"SELECT libelle AS Nom_Commune FROM commune_reference WHERE code_insee = '{insee}'")
        commune=(cur.fetchall())[0][0]
        print (commune)
        #cur.execute("SELECT obj_description(709505);")
        #print(cur.fetchall())




            #fermeture de la connexion à la base de données
        #cur.close()
        #conn.close()
        #print("La connexion PostgreSQL est fermée")
    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à PostgreSQL", error)
    
    return {"La commune recherchée est": commune}

#C:\\Users\\nicolas.malinski\\AppData\\Roaming\\Python\\Python38\\Scripts\\pipenv run uvicorn API_Light:app --reload
#pip install --user pipenv
#C:\Users\nicolas.malinski\AppData\Roaming\Python\Python39\Scripts\pipenv install fastapi uvicorn[standard]
#C:\Users\nicolas.malinski\AppData\Roaming\Python\Python39\Scripts
#C:\\Users\\nicolas.malinski\\AppData\\Roaming\\Python\\Python38\\Scripts\\pipenv run uvicorn API_V0:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs
