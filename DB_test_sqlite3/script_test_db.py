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
    ('shot_001_layout_010.max', '/path/to/shot001', '2022-01-01 12:00:00'),
    ('shot_002_rendering_005.max', '/path/to/shot002', '2022-01-02 12:00:00'),
    ('shot_003_lighting_012.max', '/path/to/shot003', '2022-01-03 12:00:00'),
    ('shot_004_layout_002.max', '/path/to/shot004', '2022-01-04 12:00:00'),
    ('shot_005_rendering_009.max', '/path/to/shot005', '2022-01-05 12:00:00'),
    ('shot_006_lighting_003.max', '/path/to/shot006', '2022-01-06 12:00:00'),
    ('shot_007_layout_015.max', '/path/to/shot007', '2022-01-07 12:00:00'),
    ('shot_008_rendering_008.max', '/path/to/shot008', '2022-01-08 12:00:00'),
    ('shot_009_lighting_001.max', '/path/to/shot009', '2022-01-09 12:00:00'),
    ('shot_010_layout_007.max', '/path/to/shot010', '2022-01-10 12:00:00'),
    ('shot_011_rendering_013.max', '/path/to/shot011', '2022-01-11 12:00:00'),
    ('shot_012_lighting_006.max', '/path/to/shot012', '2022-01-12 12:00:00'),
    ('shot_013_layout_014.max', '/path/to/shot013', '2022-01-13 12:00:00'),
    ('shot_014_rendering_011.max', '/path/to/shot014', '2022-01-14 12:00:00'),
    ('shot_015_lighting_004.max', '/path/to/shot015', '2022-01-15 12:00:00')
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

  
