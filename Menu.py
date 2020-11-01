import sys
import programa as pr
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

class fractales(QMainWindow):

    def CambiarImagenOriginal(self, costa):
        if costa != None: 
            imagen = QPixmap('Recursos/' + costa)
        else:
            imagen = QPixmap('')
        imagen.scaledToWidth(371)
        imagen.scaledToHeight(321)
        self.labelImagenOriginal.setPixmap(imagen)

    def CambiarImagenGris(self, grafico):
        imagen = QPixmap(grafico)
        imagen.scaledToWidth(371)
        imagen.scaledToHeight(321)
        self.labelImagenGris.setPixmap(imagen)

    def CambiarImagenContorno(self, contorno):
        imagen = QPixmap(contorno)
        imagen.scaledToWidth(371)
        imagen.scaledToHeight(321)
        self.labelContorno.setPixmap(imagen)
    
    def Click(self):       
        costa = self.comboBoxRegion.currentText()
        cantidad = pr.ejecutar(costa)
        self.labelDimension.setText(str(cantidad)[:6])
        self.CambiarImagenOriginal(costa)
        self.CambiarImagenContorno('grafico.png')
        self.CambiarImagenGris('gris.png')

    def LimpiarElementos(self):
        self.labelDimension.setText('')
        self.CambiarImagenOriginal(None)
        self.CambiarImagenContorno(None)
        self.CambiarImagenGris(None)

    def CambiarRegion(self):
        self.LimpiarElementos()

    def SiguienteIntegrante(self):
        actual = self.stackedIntegrantes.currentIndex()
        if actual == 4: actual = -1
        self.stackedIntegrantes.setCurrentIndex(actual + 1)

    def SiguienteHerramienta(self):
        actual = self.stackedHerramientas.currentIndex()
        if actual == 1: actual = -1
        self.stackedHerramientas.setCurrentIndex(actual + 1)

    def SiguienteNosotros(self):
        actual = self.stackedNosotros.currentIndex()
        if actual == 1: actual = -1
        self.stackedNosotros.setCurrentIndex(actual + 1)
    

    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaz/Interface.ui",self)
        self.comboBoxRegion.addItems(['Australia.jpg', 'ReinoUnido.jpg', 'BuenosAires.jpg'])
        self.labelDimension.setText('')
        self.buttonCalcularDimension.clicked.connect(self.Click)
        self.comboBoxRegion.currentIndexChanged.connect(self.CambiarRegion)
        self.commandButtonSiguiente.clicked.connect(self.SiguienteIntegrante)
        self.commandButtonSiguiente2.clicked.connect(self.SiguienteHerramienta)
        self.commandButtonSiguiente3.clicked.connect(self.SiguienteNosotros)
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI = fractales()
    GUI.show()
    pr.Borrar('gris.png', 'grafico.png')
    sys.exit(app.exec_())
