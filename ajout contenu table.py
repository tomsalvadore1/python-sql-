import sqlite3
import pandas as pd
import math

connexion = sqlite3.connect("vulog.db")
curseur = connexion.cursor()

input1 = input("id du client ")
input2 = input("nom du client ")
input3 = math.ceil(float(input("durée de la location (en minutes)")))
prix = input3 * 0.05

requete = f"INSERT INTO vulog (nom , id, temps_d_utilisation,prix ) VALUES ({input1}, '{input2}', {input3} , {prix})"
curseur.execute(requete)

connexion.commit()



curseur.close()
connexion.close()