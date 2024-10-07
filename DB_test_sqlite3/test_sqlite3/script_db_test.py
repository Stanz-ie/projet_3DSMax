import sqlite3

def create_table():
    
    connexion = sqlite3.connect("test.db")

    # objet curseur permet de faire les requêtes
    curseur = connexion.cursor()

    # recréer la table à chaque lancement du script
    curseur.execute("DROP TABLE IF EXISTS personnages_arcane")

    curseur.execute('''CREATE TABLE IF NOT EXISTS 
    personnages_arcane(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nom TEXT,
    genre TEXT,
    ville TEXT,
    statut TEXT)''' )

    connexion.close()

create_table()

######################################

# insérer des données

def inserer_perso(nom, genre, ville, statut):

    connexion = sqlite3.connect("test.db")

    curseur = connexion.cursor()

    curseur.execute('''
    INSERT INTO personnages_arcane
    (nom, genre, ville, statut)
    VALUES
    ( ?, ?, ?, ?)
    ''', (nom, genre, ville, statut))
    connexion.commit()

    connexion.close()

inserer_perso("Vi", "femme", "Zaun", "vivante")

######################################

# insérer un jeu de données

personnages_saison1 = [("Jinx", "femme", "Zaun", "vivante"), 
    ("Silco", "homme", "Zaun", "mort"), ("Jayce", "homme", "Piltover", "vivant"),
    ("Mel", "femme", "Noxus", "vivante"), ("Vander", "homme", "Zaun", "mort"),
    ("Ekko", "homme", "Zaun", "vivant"), ("Caitlyn", "femme", "Piltover", "vivante"),
    ("Mylo", "homme", "Zaun", "mort"), ("Claggor", "homme", "Zaun", "mort"),
    ("Cassandra", "femme", "Piltover", "inconnu"), ("Sevika", "femme", "Zaun", "vivante")]

def inserer_plusieurs_persos(personnages_saison1):

    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    curseur.executemany('''
    INSERT INTO personnages_arcane
    (nom, genre, ville, statut)
    VALUES 
    (?, ?, ?, ?)
    ''', personnages_saison1)

# pas besoin d'indiquer l'ID, vu que celle-ci est auto-incrémentée et n'est pas présente dans
# la liste des tuples au-dessus
    connexion.commit()
    connexion.close()

inserer_plusieurs_persos(personnages_saison1)

######################################

def recup_persos_info (id):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    res = curseur.execute("SELECT * FROM personnages_arcane WHERE id = ?", (id,))
    perso = res.fetchall()
    connexion.close()

    return perso

# print (recup_persos_info(7))

######################################

def mise_a_jour (statut):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    curseur.execute("UPDATE personnages_arcane SET statut = 'morte' WHERE statut = ?", (statut, ))
    connexion.commit()
    connexion.close()

# mise_a_jour(statut = "inconnu")

######################################

def supprimer (id):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    curseur.execute("DELETE FROM personnages_arcane WHERE id = ?", (id, ))
    connexion.commit()
    connexion.close()

# supprimer (id = "9")


# requêtes d'interrogation - méthodes fetch

# res = curseur.execute("SELECT * FROM personnages_arcane")
# print(res.fetchall())
# print (res.fetchone())
# print (res.fetchone())
# print (res.fetchmany(4))

# requête d'interrogation préparées

# res = curseur.execute("SELECT * FROM personnages_arcane WHERE ville = ?", ('Zaun',))
# print (res.fetchall())
  
