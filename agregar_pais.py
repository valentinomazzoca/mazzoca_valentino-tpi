import csv
from validaciones import validar_formato_csv

def agregar_pais(nombre, poblacion, superficie, continente):
    if nombre == "" or poblacion == "" or superficie == "" or continente == "":
        raise ValueError("Error: no se pudo agregar el país. Todos los campos son obligatorios.")

    entero_p = int(poblacion)
    entero_s = int(superficie)

    pais_agregado = [nombre, entero_p, entero_s, continente]

    with open("paises_70.csv", "a", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(pais_agregado)
        print("Pais agregado correctamente")


def modificar_poblacion_y_superficie(nombre, poblacion, superficie):
    if nombre == "" or poblacion == "" or superficie == "":
        raise ValueError("Error: todos los campos son obligatorios.")

    entero_p = int(poblacion)
    entero_s = int(superficie)

    paises = []

    with open("paises_70.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            validar_formato_csv(fila)
            paises.append(fila)

    encontrado = False

    for fila in paises[1:]:
        if fila[0].lower() == nombre.lower():
            fila[1] = entero_p
            fila[2] = entero_s
            encontrado = True

    if not encontrado:
        raise ValueError("Error: el país no existe.")

    with open("paises_70.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(paises)

    print("País modificado correctamente.")

