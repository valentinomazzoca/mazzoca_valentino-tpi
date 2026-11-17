def validar_formato_csv(fila):
    if len(fila) != 4:
        raise ValueError("Error: una fila del CSV tiene un formato incorrecto.")

    int(fila[1])
    int(fila[2])