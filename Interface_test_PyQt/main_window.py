import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget

class main_window(QMainWindow):
    
    def __init__(self):
        # constructeur parent
        super().__init__()
        # ajout de propriétés
        self.setWindowTitle("Mon Interface")
        self.setMaximumSize(500, 400)

if __name__ == "__main__":
    # On crée l'instance d'application en lui passant le tableau des arguments.
    app = QApplication(sys.argv)

    # TODO : Instancier et afficher la fenêtre graphique.
    window = main_window()
    window.show()

    # On démarre la boucle de gestion des événements.
    sys.exit(app.exec_())
