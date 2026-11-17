import csv
from validaciones import validar_formato_csv


def buscar_pais(nombre_buscado):
    paises_encontrados = []

    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)

        for fila in lector:
            validar_formato_csv(fila)
            if nombre_buscado.lower() in fila[0].lower():
                paises_encontrados.append(fila)

    return paises_encontrados