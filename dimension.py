#IMPORTAMOS LIBRERIAS NECESARIAS
import cv2
import numpy as np

def ObtenerDimension(I):
    #FUNCION DE CALCULO DE LA DIMENSION FRACTAL
    def fractal_dimension(Z, threshold=0.9):

        # Verifica que la imagen sea 2D, el metodo de BOX-COUNTING
        # empleado solo funciona con imagenes 2D
        assert(len(Z.shape) == 2)

        # Metodo Box-Counting obtenido de: https://github.com/rougier/numpy-100 (#87)
        def boxcount(Z, k):
            S = np.add.reduceat(
                np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                   np.arange(0, Z.shape[1], k), axis=1)

            # Contamos los pixeles no vacios (0) y las cajas no llenas (k*k)
            return len(np.where((S > 0) & (S < k*k))[0])


        # Convertimos a Z en un arreglo binario
        Z = (Z < threshold)

        # Toma la dimension minima de la imagen
        p = min(Z.shape)

        # Mayor potencia de 2 que sea menor o igual que p (dimension minima de la imagen)
        n = 2**np.floor(np.log(p)/np.log(2))

        # Extraemos el exponente
        n = int(np.log(n)/np.log(2))

        # Construimos sucesivas cajas de tamaños que van desde 2**n bajando hasta 2**1
        sizes = 2**np.arange(n, 1, -1)

        # Conteo actual de cajas con tamaño decreciente
        counts = []
        for size in sizes:
            counts.append(boxcount(Z, size))

        # Hallar los coeficientes del polinomio log(sizes) de grado 1 que se ajusta a los datos de
        # log (counts), minimizando la suma de los cuadrados de las desviaciones de los datos del modelo
        coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
        return -coeffs[0]

    #LECTURA DE IMAGEN EN 2 CANALES IGNORANDO EL RGB YA QUE LA CONVERTIMOS EN ESCALA DE GRISES
    imagen_2Canales = cv2.cvtColor(cv2.imread(I), cv2.COLOR_RGB2GRAY)

    #MUESTRA DE LOS DATOS OBTENIDOS
    return fractal_dimension(imagen_2Canales), (np.log(3)/np.log(2))