import sqlite3
import pandas as pd

connexion = sqlite3.connect('vulog.db') #on se connecte a la base de donnée 

query = "SELECT * FROM vulog" # requete sql pour dire "on selectionne tout"
df = pd.read_sql_query(query, connexion) #on place ce tout dans un dataframe

df.to_csv('vulog.csv', index=False, mode = "w") #on converti le data frame en csv 

connexion.close() #et on oublie pas de fermer 