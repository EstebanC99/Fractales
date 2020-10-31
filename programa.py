import grafico as gr
import dimension as dim
from os import remove, path, system

def ejecutar(direc):
    
    
    system("cls")
    direccion = direc #input('Australia.jpg')
    if 'Recursos/' not in direccion: direccion = 'Recursos/' + direccion

    try:  
        #LLAMADA A LA FUNCION DE CARGAR IMAGEN Y OBTENER CONTORNOS
        cadena_gris = gr.CargarImagen(direccion)

        #OBTENCION DE LOS VALORES DE DIMENSION FRACTAL
        box_counting, haussdorf = dim.ObtenerDimension(cadena_gris)


        #ESTA LINEA BORRA LA IMAGEN TEMPORAL DE CONTORNOS CREADA
        if path.exists(cadena_gris): remove(cadena_gris) 

        #DEVUELVE DIMENSION FRACTAL
        return (box_counting)

    except:
        #EN CASO QUE LA IMAGEN NO SE ENCUENTRE
        print('La direccion ingresada no pertenece a una imagen')

