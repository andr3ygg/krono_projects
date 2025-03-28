import os
from random import choice
from modules.frames import frames
from modules.inputs import datos_user
from modules.logic import logica


def reanudar():
    print(
        """Quieres seguir jugando? 
0 es no || 1 es sí"""
    )
    while True:
        try:
            opcion = int(input())
        except ValueError:
            print("Solamente se permiten numeros")
        if opcion == 0:
            exit()
        elif opcion == 1:
            os.system("clear")
            juego()
        else:
            print("Solamente 0 o 1")


def juego():
    opciones = ["Piedra", "Papel", "Tijera"]
    numero_partidas = 3
    puntuacion_user = 0
    puntuacion_maquina = 0
    lista_dibujos = frames

    # 2 opciones: jugar vs la maquina || juego automatico
    print("1: automatico   2: vs la maquina")
    # while True:
    juego_opcion = int(input())
    #     if juego_opcion != 1 or juego_opcion != 2 or juego_opcion isinstance(juego_opcion, str):
    #         print("Las opciones son: 1 o 2")

    if juego_opcion == 1:

        while True:
            opcion_maquina_uno = choice(opciones).capitalize()
            # DIBUJITO
            numero_posicion_dibujito = opciones.index(opcion_maquina_uno)
            print(lista_dibujos[numero_posicion_dibujito])
            opcion_maquina_dos = choice(opciones).capitalize()
            # DIBUJITO
            numero_posicion_dibujito_maquina = opciones.index(opcion_maquina_dos)
            print(lista_dibujos[numero_posicion_dibujito_maquina])
            puntuacion_user, puntuacion_maquina = logica(
                opcion_maquina_uno, opcion_maquina_dos, puntuacion_user, puntuacion_maquina
            )

            print(
                f"""
    Usuario 1: {puntuacion_user}
    Usuario 2: {puntuacion_maquina}
    """
            )

            if (
                puntuacion_user == numero_partidas - 1
                or puntuacion_maquina == numero_partidas - 1
            ):
                if puntuacion_user > puntuacion_maquina:
                    print("El usuario 1 ha ganado la partida")
                else:
                    print("La usuario 2 ha ganado la partida")

                reanudar()

    elif juego_opcion == 2:

        while True:
            opcion_usuario = datos_user()
            # DIBUJITO
            numero_posicion_dibujito = opciones.index(opcion_usuario)
            print(lista_dibujos[numero_posicion_dibujito])
            opcion_maquina = choice(opciones).capitalize()
            print(f"OPCION MAQUINA: {opcion_maquina}")
            # DIBUJITO
            numero_posicion_dibujito_maquina = opciones.index(opcion_maquina)
            print(lista_dibujos[numero_posicion_dibujito_maquina])
            puntuacion_user, puntuacion_maquina = logica(
                opcion_usuario, opcion_maquina, puntuacion_user, puntuacion_maquina
            )

            print(
                f"""
    Usuario: {puntuacion_user}
    Maquina: {puntuacion_maquina}
    """
            )

            if (
                puntuacion_user == numero_partidas - 1
                or puntuacion_maquina == numero_partidas - 1
            ):
                if puntuacion_user > puntuacion_maquina:
                    print("El usuario ha ganado la partida")
                else:
                    print("La maquina ha ganado la partida")

                reanudar()

    else:
        print("Introduce 0 o 1")


def main():
    try:
        juego()
    except KeyboardInterrupt:
        print("Bye!")


main()
