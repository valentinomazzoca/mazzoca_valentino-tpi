from filtrar_tpi import filtro_continente, rango_poblacion, rango_superficie
from agregar_pais import agregar_pais, modificar_poblacion_y_superficie
from busqueda_nombre import buscar_pais
from estadisticas_tpi import mayor_y_menor_poblacion, promedio_poblacion, promedio_superficie, cantidad_paises_continente
from ordenar_tpi import ordenar_poblacion, ordenar_nombre, ordenar_superficie

def menu_filtrar():
    print("\n===== FILTRAR PAÍSES =====")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            continente = input("Ingrese el continente que desea buscar: ")

            resultado = filtro_continente(continente)

            print("\n===== PAÍSES DEL CONTINENTE =====")
            for pais in resultado:
                print(pais)

        case "2":
            minimo = int(input("Ingrese la población mínima: "))
            maximo = int(input("Ingrese la población máxima: "))

            resultado = rango_poblacion(minimo, maximo)

            print("\n===== PAÍSES DENTRO DEL RANGO DE POBLACIÓN =====")

            if resultado:
                for pais in resultado:
                    print(pais)
                else:
                    print("No se encontraron países dentro de ese rango.")
        case "3":
            minimo = int(input("Ingrese la superficie mínima en km²: "))
            maximo = int(input("Ingrese la superficie máxima en km²: "))

            resultado = rango_superficie(minimo, maximo)

            print("\n===== PAÍSES DENTRO DEL RANGO DE SUPERFICIE =====")

            if resultado:
                for pais in resultado:
                    print(pais)
            else:
                print("No se encontraron países dentro de ese rango.")
        case _:
            print("Opción incorrecta.")


def menu_ordenar():
    print("\n===== ORDENAR PAÍSES =====")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            ascendente, descendente = ordenar_nombre()

            print("\n===== ORDEN ALFABÉTICO ASCENDENTE =====")
            for pais in ascendente:
                print(pais)

            print("\n===== ORDEN ALFABÉTICO DESCENDENTE =====")
            for pais in descendente:
                print(pais)
        case "2":
            ascendente, descendente = ordenar_poblacion()

            print("\n===== POBLACIÓN: MENOR A MAYOR =====")
            for pais in ascendente:
                print(pais)

            print("\n===== POBLACIÓN: MAYOR A MENOR =====")
            for pais in descendente:
                print(pais)

        case "3":
            ascendente, descendente = ordenar_superficie()

            print("\n===== SUPERFICIE: MENOR A MAYOR =====")
            for pais in ascendente:
                print(pais)

            print("\n===== SUPERFICIE: MAYOR A MENOR =====")
            for pais in descendente:
                print(pais)

        case _:
            print("Opción incorrecta.")


def menu_estadisticas():
    print("\n===== ESTADÍSTICAS =====")
    print("1. Mayor y menor población")
    print("2. Promedio de población")
    print("3. Promedio de superficie")
    print("4. Cantidad de países por continente")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            pais_mayor, mayor_poblacion, pais_menor, menor_poblacion = mayor_y_menor_poblacion()

            print("\n===== MAYOR Y MENOR POBLACIÓN =====")
            print(f"País con mayor población: {pais_mayor}")
            print(f"Población: {mayor_poblacion:,}")

            print(f"\nPaís con menor población: {pais_menor}")
            print(f"Población: {menor_poblacion:,}")

        case "2":
            promedio = promedio_poblacion()

            print("\n===== PROMEDIO DE POBLACIÓN =====")
            print(f"El promedio de población de los países es: {promedio:,.2f} habitantes")
        case "3":
            promedio = promedio_superficie()

            print("\n===== PROMEDIO DE SUPERFICIE =====")
            print(f"El promedio de superficie de los países es: {promedio:,.2f} km²")

        case "4":
            america, europa, asia, africa, oceania, europa_asia = cantidad_paises_continente()

            print("\n===== CANTIDAD DE PAÍSES POR CONTINENTE =====")
            print(f"América: {america}")
            print(f"Europa: {europa}")
            print(f"Asia: {asia}")
            print(f"África: {africa}")
            print(f"Oceanía: {oceania}")
            print(f"Europa/Asia: {europa_asia}")
        case _:
            print("Opción incorrecta.")


def menu():
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE PAÍSES =====")
        print("1. Agregar país")
        print("2. Actualizar población y superficie")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del país: ")
                poblacion = input("Ingrese la población: ")
                superficie = input("Ingrese la superficie en km²: ")
                continente = input("Ingrese el continente: ")

                try:
                    agregar_pais(nombre, poblacion, superficie, continente)

                except ValueError as error:
                    print(error)

            case "2":
                nombre = input("Ingrese el nombre del país que desea modificar: ")
                poblacion = input("Ingrese la nueva población: ")
                superficie = input("Ingrese la nueva superficie en km²: ")

                try:
                    modificar_poblacion_y_superficie(nombre, poblacion, superficie)

                except ValueError as error:
                    print(error)
            case "3":
                nombre_buscado = input("Ingrese el nombre del país que desea buscar: ")

                resultado = buscar_pais(nombre_buscado)

                print("\n===== RESULTADOS DE BÚSQUEDA =====")

                if resultado:
                    for pais in resultado:
                        print(f"Nombre: {pais[0]}")
                        print(f"Población: {pais[1]}")
                        print(f"Superficie: {pais[2]} km²")
                        print(f"Continente: {pais[3]}")
                        print("-------------------------")
                else:
                    print("No se encontraron países.")
            case "4":
                menu_filtrar()

            case "5":
                menu_ordenar()

            case "6":
                menu_estadisticas()

            case "7":
                print("¡Gracias por utilizar el sistema!")
                break

            case _:
                print("Opción incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    menu()
