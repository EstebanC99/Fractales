import sys
import programa as pr
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class ejemplo_prueba(QMainWindow):


    def Click(self):
        def CambiarImagen():
            imagen = QPixmap('Recursos/' + self.comboBox.currentText())
            imagen.scaledToWidth(800)
            imagen.scaledToHeight(600)
            self.label2.resize(imagen.width(), imagen.height())
            self.label2.setPixmap(imagen)
            
        
        cantidad = pr.ejecutar(self.comboBox.currentText())
        self.label.setText(str(cantidad)[:6])
        CambiarImagen()

    

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.menu.ui",self)
        self.comboBox.addItems(['Australia.jpg', 'ReinoUnido.jpg', 'BuenosAires.jpg'])
        self.pushButton.clicked.connect(self.Click)
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI = ejemplo_prueba()
    GUI.show()
    sys.exit(app.exec_())
