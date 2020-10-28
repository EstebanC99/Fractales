#IMPORTAMOS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt

#CARGAMOS IMAGENES
imagen_original = cv2.imread(r'Australia.jpg')
imagen_blanca = cv2.imread(r'Fondo.jpg')

#CONVERTIMOS DE BGR A RGB Y A GRIS
imagen_orginal = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_RGB2GRAY)

#CREACION DE IMAGEN BINARIA DE GRIS
_, binaria = cv2.threshold(imagen_gris, 225, 255, cv2.THRESH_BINARY_INV)

#EXTRACCION DEL CONTORNO DE LA IMAGEN
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#DIBUJA EL CONTORNO SOBRE EL FONDO BLANCO
imagen_blanca = cv2.drawContours(imagen_blanca, contornos, -1, (0, 0, 0), 2)

#MUESTRA DE LA IMAGEN FINAL
plt.imshow(imagen_blanca)
plt.show()
