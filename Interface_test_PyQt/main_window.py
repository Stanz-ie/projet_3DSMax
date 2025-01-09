import sys
sys.path.append('/home/constance/Documents/ADA/PROJETS_PERSOS/projet_3DSMax/projet_3DSMax_code')
from DB_test_sqlite3.script_test_db import create_table, insert_shot, insert_all_shots, update_shot, delete_shot

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QScrollArea, 
QLineEdit, QHBoxLayout, QFrame, QPushButton, QLabel)

from datetime import datetime


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__() # constructeur parent (QMainWindow)
        self.setWindowTitle("Mon Interface") # ajout de propriétés
        #self.setMaximumSize(500, 400)
        create_table()
    
def main():
    app = QApplication(sys.argv) # On crée l'instance d'application
    # possible de créer l'instance sans liste d'arguments (si on sait qu'on
    # utilisera pas le terminal pour controler QT
    # dans ce cas, juste créer une liste vide app = QApplication([]) 
    app.setStyle('fusion')
    win = MainWindow()
    win.show() # Afficher la fenêtre (par défaut elle ne l'est pas)
    app.exec_() # On démarre la boucle de gestion des événements.

if __name__ == "__main__":
    main()


    
    