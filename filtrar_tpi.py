# Filtrar países por:
# Continente
# Rango de población
# Rango de superficie

import csv
def filtro_continente(continente_buscado):
    continente_elegido = []
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            if continente_buscado.lower() == fila[3].lower():
                continente_elegido.append(fila[3])
    return continente_elegido

def rango_poblacion(minimo, maximo):
    dentro_rango = []
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            entero = int(fila[1])
            if minimo <= entero and maximo >= entero:
                dentro_rango.append(fila)
    return dentro_rango

def rango_superficie(minimo, maximo):
    dentro_rango = []
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            entero = int(fila[2])
            if minimo <= entero and maximo >= entero:
                dentro_rango.append(fila)
    return dentro_rango