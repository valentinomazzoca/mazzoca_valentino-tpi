#Ordenar países por:
# Nombre
# Población
# Superficie (ascendente o descendente)

import csv

def ordenar_poblacion():
    orden_ascendente = []
    orden_descendente = []

    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        poblaciones = []

        next(lector)

        for filas in lector:
            poblacion = int(filas[1])
            poblaciones.append(poblacion)

        orden_ascendente = sorted(poblaciones)
        orden_descendente = sorted(poblaciones, reverse=True)

    return orden_ascendente, orden_descendente
