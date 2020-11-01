import sys
import programa as pr
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class fractales(QMainWindow):


    def Click(self):
        def CambiarImagen():
            imagen = QPixmap('gris.png')
            imagen.scaledToWidth(281)
            imagen.scaledToHeight(271)
            self.labelImagen.resize(281, 271)
            self.labelImagen.setPixmap(imagen)
            
        
        cantidad = pr.ejecutar(self.comboBox.currentText())
        self.labelDimension.setText(str(cantidad)[:6])
        CambiarImagen()

    

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI.menu.ui",self)
        self.comboBox.addItems(['Australia.jpg', 'ReinoUnido.jpg', 'BuenosAires.jpg'])
        self.labelDimension.setText('')
        self.labelImagen.setText('')
        self.buttonCalcularDimension.clicked.connect(self.Click)
        

def Iniciar():
    if __name__=='__main__':
        app=QApplication(sys.argv)
        GUI = fractales()
        GUI.show()
        pr.Borrar('gris.png')
        sys.exit(app.exec_())
