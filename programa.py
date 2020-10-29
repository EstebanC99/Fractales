import grafico as gr
import dimension as dim
from os import remove, path

def MostrarDatos(B, H):
    print("Dimension de Minkowski–Bouligand calculada: ", B)
    print("Dimension teorica de Haussdorf:        ", H)
    print("Tal como se ve, un objeto tiene dimension fractal si esta es menor a la dimension de Haussdorf")


try: 
    #LLAMADA A LA FUNCION DE CARGAR IMAGEN Y OBTENER CONTORNOS
    cadena_gris = gr.CargarImagen(input('Ingrese ubicacion de la imagen:'))

    #OBTENCION DE LOS VALORES DE DIMENSION FRACTAL
    box_counting, haussdorf = dim.ObtenerDimension(cadena_gris)

    #MUESTREO DE DATOS
    MostrarDatos(box_counting, haussdorf)

    #ESTA LINEA BORRA LA IMAGEN TEMPORAL DE CONTORNOS CREADA
    if path.exists(cadena_gris): remove(cadena_gris) 


except:
    #EN CASO QUE LA IMAGEN NO SE ENCUENTRE
    print('La direccion ingresada no pertenece a una imagen')

