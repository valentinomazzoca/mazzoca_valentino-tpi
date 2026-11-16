#Ordenar países por:
# Nombre
# Población
# Superficie (ascendente o descendente)

import csv


def ordenar_poblacion():
    poblacion = []

    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for filas in lector:
            poblacion.append(filas)

        orden_ascendente = sorted(poblacion, key=lambda fila: int(fila[1]))
        orden_descendente = sorted(poblacion, key=lambda fila: int(fila[1]), reverse=True)

    return orden_ascendente, orden_descendente

def ordenar_nombre():
    nombre = []
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for filas in lector:
            nombre.append(filas)

        orden_ascendente = sorted(nombre, key=lambda fila: fila[0])
        orden_descendente = sorted(nombre, key=lambda fila: fila[0], reverse= True)
    return orden_ascendente, orden_descendente

def ordenar_superficie():
    superficie = []
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for filas in lector: 
            superficie.append(filas)
            orden_ascendente = sorted(superficie, key=lambda fila: int(fila[2]))
            orden_descendente = sorted(superficie, key=lambda fila: int(fila[2]), reverse= True)
    return orden_ascendente, orden_descendente
        