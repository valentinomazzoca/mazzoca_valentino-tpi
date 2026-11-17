
import csv
from validaciones import validar_formato_csv

def mayor_y_menor_poblacion():

    mayor_poblacion = 0
    menor_poblacion = float("inf")

    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for fila in lector:
            validar_formato_csv(fila)
            poblacion = int(fila[1])

            if poblacion < menor_poblacion:
                menor_poblacion = poblacion
                pais_menor = fila[0]

            if poblacion > mayor_poblacion:
                mayor_poblacion = poblacion
                pais_mayor = fila[0]

    return pais_mayor, mayor_poblacion, pais_menor, menor_poblacion

def promedio_poblacion():
    cantidad_paises = 0
    cantidad_habitantes = 0
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        next(lector)

        for fila in lector:
            validar_formato_csv(fila)
            poblacion = int(fila[1])
            cantidad_habitantes += poblacion
            cantidad_paises += 1
    promedio_final = cantidad_habitantes / cantidad_paises

    return promedio_final

def promedio_superficie():
    cantidad_paises = 0
    cantidad_superficie = 0
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)

        for fila in lector:
            validar_formato_csv(fila)
            superficie = int(fila[2])
            cantidad_superficie += superficie
            cantidad_paises += 1
    promedio_final = cantidad_superficie / cantidad_paises
    return promedio_final

def cantidad_paises_continente():
    cantidad_america = 0
    cantidad_europa = 0
    cantidad_asia = 0
    cantidad_africa = 0
    cantidad_oceania = 0
    cantidad_europa_asia = 0    
    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            validar_formato_csv(fila)
            continente = (fila[3]).lower()
            if continente == "america":
                cantidad_america += 1
            elif continente == "europa":
                cantidad_europa += 1
            elif continente == "asia":
                cantidad_asia += 1
            elif continente == "africa":
                cantidad_africa += 1
            elif continente == "oceania":
                cantidad_oceania += 1
            elif continente == "europa/asia":
                cantidad_europa_asia += 1
    return cantidad_america, cantidad_europa, cantidad_asia, cantidad_africa, cantidad_oceania, cantidad_europa_asia