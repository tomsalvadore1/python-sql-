import sqlite3

connexion = sqlite3.connect("vulog.db")
curseur = connexion.cursor() 


curseur.execute("CREATE TABLE vulog (nom TEXT, id INTEGER, temps_d_utilisation INTEGER, prix FLOAT)") #requete de creation de la table 



connexion.commit() #pour dire de sauvegarder les changements 

connexion.close() #a ne pas oublier 