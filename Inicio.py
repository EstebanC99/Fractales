import sys
import programa as pr
import Menu
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class inicio(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.inicio.ui",self)
        self.menuButton.clicked.connect(Menu.Iniciar())



if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI = inicio()
    GUI.show()
    sys.exit(app.exec_())