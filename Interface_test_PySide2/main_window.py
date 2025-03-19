import re
import sys
sys.path.append('/home/constance/Documents/DEV/PROJETS_PERSOS/projet_3DSMax/projet_3DSMax_code')
from DB_test_sqlite3.script_test_db import create_table, insert_shot, update_shot, delete_shot

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QVBoxLayout, QScrollArea, 
                               QLineEdit, QDateEdit, 
                               QFormLayout, QPushButton, QLabel)

class MainWindow(QMainWindow):
    
    def __init__(self):
        # constructeur parent (QMainWindow)
        super().__init__()
       
        self.setWindowTitle("Mon Interface POC")
        self.setFixedSize(400, 300)

        central_area = QWidget()
        self.setCentralWidget(central_area)

        self.shot_name = QLineEdit()
        self.shot_name.setPlaceholderText('shot_001_layout_010.max')
        self.path = QLineEdit()
        self.path.setPlaceholderText('/path/to/shot_001_layout_010.max')
        self.date_entry = QDateEdit()
        self.add_button1 = QPushButton(text="Ajouter shot")
        self.add_button2 = QPushButton(text="Supprimer shot")

        # Connecter le bouton à la fonction add_shot ou delete_shot
        self.add_button1.clicked.connect(self.add_shot)
        self.add_button2.clicked.connect(self.delete_shot)

        central_area = QWidget()
        self.setCentralWidget(central_area)

        form_layout = QFormLayout()
        form_layout.addRow('Nom du shot', self.shot_name)
        form_layout.addRow('Chemin du shot', self.path)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.add_button1)
        layout.addWidget(self.add_button2)
        central_area.setLayout(layout)

        create_table()
        
    def add_shot(self):
        shot_name = self.shot_name.text()
        pattern_shot_name = re.compile(r'^shot_\d{3}_(layout|lighting|rendering)_\d{3}.max$')
        
        if not pattern_shot_name.match(shot_name):
            print('Nom de shot invalide')
            return # on sort de la fonction
      
        path = self.path.text()
        pattern_path_name = re.compile(r'^/path/to/shot_\d{3}_(layout|lighting|rendering)_\d{3}.max$')
        
        if not pattern_path_name.match(path):
            print('Chemin de shot invalide')
            return

        try:
            if shot_name and path:
                insert_shot(shot_name, path)
            self.shot_name.clear()  
            self.path.clear()
            print('Shot ajouté')
        except:
            print('Erreur lors de l\'ajout du shot')

    def delete_shot(self):
        shot_name = self.shot_name.text()
        path = self.path.text()
        if shot_name and path:
            delete_shot(shot_name, path)
            self.shot_name.clear()  
            self.path.clear()
    
    
# si on sait qu'on n'utilisera pas le terminal pour controler QT
# dans ce cas, juste créer une liste vide app = QApplication([])
app = QApplication(sys.argv)  
app.setStyle('fusion')
win = MainWindow()
# Afficher la fenêtre (par défaut elle ne l'est pas)
win.show()
# On démarre la boucle de gestion des événements. 
app.exec_()

    

    
    


   


   


    
    