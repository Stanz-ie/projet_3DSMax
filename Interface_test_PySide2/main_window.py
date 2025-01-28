import sys
sys.path.append('/home/constance/Documents/ADA/PROJETS_PERSOS/projet_3DSMax/projet_3DSMax_code')
from DB_test_sqlite3.script_test_db import create_table, insert_shot, insert_all_shots, update_shot, delete_shot

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea, 
QLineEdit, QDateEdit, QHBoxLayout, QFrame, QPushButton, QLabel)
from PySide2.QtGui import QPalette, QColor

from datetime import datetime

'''
class CreateRecord(QFrame):
    def __init__(self, main_window):
        super().__init__()
        self.date_entry = QDateEdit()
        self.shot_name = QLineEdit()
        self.shot_name.setPlaceholderText('Shot name')
        self.path = QLineEdit()
        self.path.setPlaceholderText('/path/to/shot')
        self.add_button = QPushButton(text="Add Shot")
        # Connecter le bouton à la fonction add_shot
        self.add_button.clicked.connect(self.add_shot)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel('Shot Name:'))
        layout.addWidget(self.shot_name)
        layout.addWidget(QLabel('Completed Date:'))
        layout.addWidget(self.date_entry)
        layout.addWidget(self.add_button)

    def add_shot(self):
        shot_name = self.shot_name.text()
        completed_date = self.date_entry.date().toString("yyyy-MM-dd")
        path = self.path.text()
        if shot_name and path:
            insert_shot(shot_name, completed_date, path)
            # Recharger la DB après ajout d'un plan
            #self.main_window.load_collection()
            # Effacer le champ de saisie
            self.shot_name.clear()  
            self.path.clear()

class Color(QWidget):

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
'''
class MainWindow(QMainWindow):
    
    def __init__(self):
        # constructeur parent (QMainWindow)
        super().__init__()
       
        self.setWindowTitle("Mon Interface")
        self.setFixedSize(700, 600)

        '''
       layout = QVBoxLayout()

        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('red'))
        layout.addWidget(Color('purple'))
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        '''
 
        #create_table()

def main():
    
    # On crée l'instance d'application
    # si on sait qu'on n'utilisera pas le terminal pour controler QT
    # dans ce cas, juste créer une liste vide app = QApplication([])
    app = QApplication([])  
    app.setStyle('fusion')
    win = MainWindow()
    # Afficher la fenêtre (par défaut elle ne l'est pas)
    win.show()
    # On démarre la boucle de gestion des événements. 
    app.exec_()

if __name__ == '__main__':
    main()

#Color('red')
     
'''
    def initUI(self):
        self.main_frame = QFrame()
        self.main_layout = QVBoxLayout(self.main_frame)
    # Create an instance of CreateRecord
    # Pass a reference to the main window
        self.register_widget = CreateRecord(self)
        self.main_layout.addWidget(self.register_widget)
        self.setCentralWidget(self.main_frame)
'''    


    
    