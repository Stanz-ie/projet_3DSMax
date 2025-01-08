import sqlite3

def create_table():
    
    connexion = sqlite3.connect("test.db")

    # objet curseur permet de faire les requêtes
    curseur = connexion.cursor()

    query = '''CREATE TABLE IF NOT EXISTS 
    SHOTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    path TEXT NOT NULL,
    created_at DATETIME default current_timestamp,
    completed_at DATETIME NOT NULL )'''

    # recréer la table à chaque lancement du script
    curseur.execute("DROP TABLE IF EXISTS SHOTS")

    curseur.execute(query)

    connexion.close()

create_table()

######################################

# insérer des données

def insert_shot(name, path, completed_at):

    connexion = sqlite3.connect("test.db")

    curseur = connexion.cursor()

    query = '''
    INSERT INTO SHOTS
    (name, path, completed_at)
    VALUES
    ( ?, ?, ?)
    '''
    curseur.execute(query, (name, path, completed_at))

    connexion.commit()

    connexion.close()

insert_shot("shot_001", "/path/to/shot_001", "2022-01-01 12:00:00")

######################################

# insérer un jeu de données

all_shots = [
    ('shot_002', '/path/to/shot_002', '2022-01-02 13:00:00'),
    ('shot_003', '/path/to/shot_003', '2022-01-03 14:00:00'),
    ('shot_004', '/path/to/shot_004', '2022-01-04 15:00:00'),
    ('shot_005', '/path/to/shot_005', '2022-01-05 16:00:00'),
    ('shot_006', '/path/to/shot_006', '2022-01-06 17:00:00'),
    ('shot_007', '/path/to/shot_007', '2022-01-07 18:00:00'),
    ('shot_008', '/path/to/shot_008', '2022-01-08 19:00:00'),
    ('shot_009', '/path/to/shot_009', '2022-01-09 20:00:00'),
    ('shot_010', '/path/to/shot_010', '2022-01-10 21:00:00'),
    ('shot_011', '/path/to/shot_011', '2022-01-11 22:00:00'),
    ('shot_012', '/path/to/shot_012', '2022-01-12 23:00:00'),
    ('shot_013', '/path/to/shot_013', '2022-01-13 00:00:00'),
    ('shot_014', '/path/to/shot_014', '2022-01-14 01:00:00'),
    ('shot_015', '/path/to/shot_015', '2022-01-15 02:00:00'),
]


def insert_all_shots(all_shots):

    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    query = '''
    INSERT INTO SHOTS
    (name, path, completed_at)
    VALUES 
    (?, ?, ?)
    '''
    curseur.executemany(query, (all_shots))

# pas besoin d'indiquer l'ID, vu que celle-ci est auto-incrémentée 
# et n'est pas présente dans la liste des tuples au-dessus
    connexion.commit()
    connexion.close()

insert_all_shots(all_shots)

######################################

# récupérer les infos d'un plan par son ID

def get_shot (id):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    query = '''
    SELECT * FROM SHOTS WHERE id = ?
    '''
    res = curseur.execute(query, (id,))
    shot = res.fetchall()
    connexion.close()

    return shot

# print (get_shot(7))

######################################

def update_shot (shot_id, updated_name, updated_path, updated_completed_date):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    query = '''
    UPDATE SHOTS 
    SET name=?, path=?, completed_at=?
    WHERE id=?
    '''
    curseur.execute(query, (updated_name, updated_path, updated_completed_date, shot_id))
    connexion.commit()
    connexion.close()

#update_shot("7", "toto","/path/to/toto", "2022-01-07 18:15:00" )

######################################

def delete_shot (id):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    query = '''
    DELETE FROM SHOTS WHERE id = ?
    '''
    curseur.execute(query, (id,))
    connexion.commit()
    connexion.close()

# delete_shot (9)

  
