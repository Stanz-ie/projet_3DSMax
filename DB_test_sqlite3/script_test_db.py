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
    created_at DATETIME default current_timestamp)'''

    # recréer la table à chaque lancement du script
    curseur.execute("DROP TABLE IF EXISTS SHOTS")

    curseur.execute(query)

    connexion.close()

create_table()

######################################

# insérer des données

def insert_shot(name, path):

    connexion = sqlite3.connect("test.db")

    curseur = connexion.cursor()

    query = '''
    INSERT INTO SHOTS
    (name, path)
    VALUES
    ( ?, ?)
    '''
    curseur.execute(query, (name, path))

    connexion.commit()

    connexion.close()

insert_shot("shot_001_layout_010.max", "/path/to/shot_001_layout_010.max")

######################################

# insérer un jeu de données

all_shots = [
    ('shot_002_rendering_005.max', '/path/to/shot002_rendering_005.max'),
    ('shot_003_lighting_012.max', '/path/to/shot003_lighting_012.max'),
    ('shot_004_layout_002.max', '/path/to/shot004_layout_002.max'),
    ('shot_005_rendering_009.max', '/path/to/shot005_rendering_009.max'),
    ('shot_006_lighting_003.max', '/path/to/shot006_lighting_003.max'),
    ('shot_007_layout_015.max', '/path/to/shot007_layout_015.max'),
    ('shot_008_rendering_008.max', '/path/to/shot008_rendering_008.max'),
    ('shot_009_lighting_001.max', '/path/to/shot009_lighting_001.max'),
    ('shot_010_layout_007.max', '/path/to/shot010_layout_007.max'),
    ('shot_011_rendering_013.max', '/path/to/shot011_rendering_013.max'),
    ('shot_012_lighting_006.max', '/path/to/shot012_lighting_006.max'),
    ('shot_013_layout_014.max', '/path/to/shot013_layout_014.max'),
    ('shot_014_rendering_011.max', '/path/to/shot014_rendering_011.max'),
    ('shot_015_lighting_004.max', '/path/to/shot015_lighting_004.max')
]


def insert_all_shots(all_shots):

    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    query = '''
    INSERT INTO SHOTS
    (name, path)
    VALUES 
    (?, ?)
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

def update_shot (shot_id, updated_name, updated_path):
    connexion = sqlite3.connect("test.db")
    curseur = connexion.cursor()
    query = '''
    UPDATE SHOTS 
    SET name=?, path=?
    WHERE id=?
    '''
    curseur.execute(query, (updated_name, updated_path, shot_id))
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

  
