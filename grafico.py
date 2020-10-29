#IMPORTAMOS LIBRERIAS NECESARIAS
import cv2
import matplotlib.pyplot as plt
import numpy as np


#CARGAMOS IMAGENES
imagen_original = cv2.imread(r'ReinoUnido.jpg')
ancho, alto, canal = imagen_original.shape
imagen_blanca = np.ones((ancho, alto, canal), np.uint8)*255 #Imagen blanca sobre la que se dibuja el contorno

#CONVERTIMOS DE BGR A RGB Y A GRIS
imagen_orginal = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_RGB2GRAY)
plt.imshow(imagen_gris)
plt.show()

#CREACION DE IMAGEN BINARIA DE GRIS
_, binaria = cv2.threshold(imagen_gris, 215, 255, cv2.THRESH_BINARY_INV)
plt.imshow(binaria, cmap="gray")
plt.show()

#EXTRACCION DEL CONTORNO DE LA IMAGEN
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#DIBUJA EL CONTORNO SOBRE EL FONDO BLANCO
imagen_blanca = cv2.drawContours(imagen_blanca, contornos, -1, (0, 0, 0), 1)

#MUESTRA DE LA IMAGEN FINAL
cv2.imwrite('gris.png', imagen_blanca)
cv2.destroyAllWindows()
