def solicitar_edad():
    """
    Solicita la edad al usuario y valida la entrada Numérica y rango.
    """
    while True:
        entrada = input("Introduce tu edad: ")
        try:
            edad = int(entrada)
            if edad < 0 or edad > 120:
                raise ValueError("La edad debe estar entre 0 y 120.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, intenta de nuevo.")
        else:
            print(f"Edad válida: {edad}")
            return edad
       
# Descomentar la siguiente línea para ejecutar el programa:
solicitar_edad()