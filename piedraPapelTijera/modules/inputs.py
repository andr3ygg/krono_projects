def datos_user():
    while True:
        opcion_usuario = str(input("¿Piedra, Papel o Tijera?: ")).capitalize()
        if opcion_usuario == "Piedra" or opcion_usuario == "Papel" or opcion_usuario == "Tijera":
            return opcion_usuario
        else:
            print("Solo puedes introducir: Piedra, Papel o Tijera")
