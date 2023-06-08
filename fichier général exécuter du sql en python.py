import sqlite3


connexion = sqlite3.connect('basededonnées.db')  


trucsql = connexion.cursor()

requete = "SELECT colonne1,colonne2 FROM table WHERE condition = 'ce qu'on veut'" # attention a la difference entre ' et " ici


trucsql.execute(requete)


resultats = trucsql.fetchall()


for ligne in resultats:
    # voir sheet pandas 
    pass


trucsql.close()
connexion.close() #attention a pas oublier ca 