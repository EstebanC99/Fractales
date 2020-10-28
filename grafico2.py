import cv2
import matplotlib.pyplot as plt

imagen_original = cv2.imread(r'Australia.jpg')
imagen_blanca = cv2.imread(r'Fondo.jpg')
imagen_orginal = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)

imagen_gris = cv2.cvtColor(imagen_original, cv2.COLOR_RGB2GRAY)

_, binaria = cv2.threshold(imagen_gris, 225, 255, cv2.THRESH_BINARY_INV)

plt.imshow(binaria, cmap="gray")
plt.show()

contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


imagen_blanca = cv2.drawContours(imagen_blanca, contornos, -1, (0, 0, 0), 2)

plt.imshow(imagen_blanca)
plt.show()
