#IMPORTAMOS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt
import numpy as np


#CARGAMOS IMAGENES
def CargarImagen(path):
    
    def ConvertirAGris(IO):
        #CONVERTIMOS DE BGR A RGB Y A GRIS
        IO = cv2.cvtColor(IO, cv2.COLOR_BGR2RGB)
        IG = cv2.cvtColor(IO, cv2.COLOR_RGB2GRAY)
        return IG
    
    imagen_original = cv2.imread(path)
    tamaños = imagen_original.shape[:2]
    imagen_blanca = np.ones(tamaños, np.uint8)*255 #Imagen blanca sobre la que se dibuja el contorno
    imagen_gris = ConvertirAGris(imagen_original)


    #CREACION DE IMAGEN BINARIA DE GRIS
    #_, binaria = cv2.threshold(imagen_gris, 85, 255, cv2.THRESH_BINARY_INV) #--> Ejemplo para mar Caspio
    _, binaria = cv2.threshold(imagen_gris, 220, 255, cv2.THRESH_BINARY_INV)


    #EXTRACCION DEL CONTORNO DE LA IMAGEN
    #contornos, _ = cv2.findContours(binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #--> Trae todos los contornos, inclusive los interiores
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #--> Trae contornos exteriores
    

    #DIBUJA EL CONTORNO SOBRE EL FONDO BLANCO
    imagen_blanca = cv2.drawContours(imagen_blanca, contornos, -1, (0, 0, 0), 1)


    #MUESTRA DE LA IMAGEN FINAL
    cv2.imwrite('gris.png', imagen_blanca)
    plt.imshow(binaria, cmap="gray")
    plt.savefig("grafico.png", bbox_inches='tight')

    return 'gris.png'

