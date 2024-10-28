import sys
import os
import sqlite3

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QScrollArea, 
QLineEdit, QHBoxLayout, QFrame, QPushButton, QLabel)

'''
chemin vers la BDD utilisant la fonction os.path.dirname pour trouver le répertoire qui contient la BDD et  
la fonction os.path.join pour lier le chemin de l'interface au chemin de la bdd pour créer un chemin complet
''' 
# db_path = os.path.join(os.path.dirname(__file__), '..', 'DB_test_sqlite3', 'test.db')
db_path = '/home/constance/Documents/ADA/PROJETS_PERSOS/projet_3DSMax/projet_3DSMax_code/DB_test_sqlite3/test.db'

# ajout chemin contenant le fichier Python contenant mes fonctions liées à la BDD à la variable d'environnement
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'DB_test_sqlite3'))
sys.path.append('/home/constance/Documents/ADA/PROJETS_PERSOS/projet_3DSMax/projet_3DSMax_code/DB_test_sqlite3/script_test_db.py')

import script_test_db

class main_window(QMainWindow):
    
    def __init__(self):
        # constructeur parent (QMainWindow)
        super().__init__()
        # ajout de propriétés
        self.setWindowTitle("Mon Interface")
        self.setMaximumSize(500, 400)

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # Instancier et afficher la fenêtre graphique.
    window = main_window()
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec_())
