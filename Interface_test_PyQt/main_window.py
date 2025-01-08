import sys
sys.path.append('/home/constance/Documents/ADA/PROJETS_PERSOS/projet_3DSMax/projet_3DSMax_code')
from DB_test_sqlite3.script_test_db import create_table, insert_shot, insert_all_shots, update_shot, delete_shot

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QScrollArea, 
QLineEdit, QHBoxLayout, QFrame, QPushButton, QLabel)

from datetime import datetime


class Main(QMainWindow):
    
    def __init__(self):
        # constructeur parent (QMainWindow)
        super().__init__()
        # ajout de propriétés
        self.setWindowTitle("Mon Interface")
        #self.setMaximumSize(500, 400)
        create_table()
    
def main():
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    win = Main()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
    # On crée l'instance d'application en lui passant le tableau des arguments.
    #app = QApplication(sys.argv)

    # Instancier et afficher la fenêtre graphique.
    #window = main_window()
    #window.show()

    # On démarre la boucle de gestion des événements.
    #sys.exit(app.exec_())
