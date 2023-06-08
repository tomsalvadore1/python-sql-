import sqlite3
connexion = sqlite3.connect("")
curseur = connexion.cursor()
requetesql = "DELETE FROM table WHERE temps_utilisation < 0"
curseur.execute(requetesql)
connexion.commit
curseur.close()
connexion.close()
