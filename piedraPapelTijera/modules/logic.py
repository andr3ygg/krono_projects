def logica(usuario, maquina, puntos_user, puntos_maquina):
    # Opción 1
    if usuario == "Piedra" and maquina == "Tijera":
        print("Gana el usuario 1")
        puntos_user += 1
    elif maquina == "Piedra" and usuario == "Tijera":
        print("Gana el usuario 2")
        puntos_maquina += 1

    # Opción 2
    elif usuario == "Papel" and maquina == "Piedra":
        print("Gana el usuario 1")
        puntos_user += 1

    elif maquina == "Papel" and usuario == "Piedra":
        print("Gana el usuario 2")
        puntos_maquina += 1

    # Opción 3
    elif usuario == "Tijera" and maquina == "Papel":
        print("Gana el usuario 1")
        puntos_user += 1

    elif maquina == "Tijera" and usuario == "Papel":
        print("Gana el usuario 2")
        puntos_maquina += 1

    elif usuario == maquina:
        print("Empate")

    return puntos_user, puntos_maquina

