from random import choice
import os
import unidecode
from modules.palabras_ahorcado import palabras
from modules.ascii_ahorcado import lista_ascii


def mostrar_guiones(longitud_lista):
    guiones = []
    for i in range(longitud_lista):
        guiones.append("_")
    print(" ".join(guiones))
    return guiones


def mostrar_ascii(contador):
    LISTA_ASCII = lista_ascii
    return LISTA_ASCII[contador]


def ingresar_letras():
    auxiliar = True
    try:
        while auxiliar:
            letra = str(input("Ingresar una letra: "))

            if len(letra) > 1:
                print("Solo se puede introducir una letra")
            elif len(letra) < 1:
                print("Tienes que ingresar una letra")
            else:
                return letra
    except ValueError as err:
        print("Ha ocurrido un error", err)


def letra_en_palabra(palabra, letra, palabra_adivinada, contador):
    condicion = True
    letras_ingresadas = []
    letra = letra
    while condicion:
        if letra not in palabra_adivinada:
            if letra.lower() in unidecode.unidecode(palabra.lower()):
                for item in range(len(palabra)):
                    if letra.lower() in unidecode.unidecode(palabra.lower())[item]:
                        letras_ingresadas.append(letra)
                        palabra_adivinada[item] = palabra[item]
                condicion = False
                print(" ".join(palabra_adivinada))
            else:
                os.system("clear")
                print(" ".join(palabra_adivinada))
                print(f"{letra} no está")
                letras_ingresadas.append(letra)
                contador += 1
                print(mostrar_ascii(contador))
                print(f"Te quedan {6-contador} intentos")
                condicion = False
        else:
            print(f"{letra} ya está, ingresa otra")
            condicion = False

    return palabra_adivinada, contador


def reanudar():
    print("""¿Quieres continuar?
0 = NO
1 = SI""")
    while True:
        condicion = input("¿Quieres continuar? ")
        if condicion == "1":
            os.system("clear")
            juego()
        elif condicion == "0":
            exit()
        else:
            print("Ingresa un valor")


def juego():
    LISTA_PALABRAS = palabras
    # palabra_seleccionada = seleccionar_palabra(LISTA_PALABRAS)
    palabra_seleccionada = choice(LISTA_PALABRAS)
    # print(palabra_seleccionada)
    maximo_intentos = 6  # Change names
    contador = 0  # Change names x2
    # auxiliar_letra_en_palabra = True
    print(mostrar_ascii(contador))
    guiones = mostrar_guiones(len(palabra_seleccionada))
    print()

    while contador <= maximo_intentos:
        letra = ingresar_letras()
        # Cambiamos el valor del guión bajo por la letra introducida (palabra)
        guiones, contador = letra_en_palabra(palabra_seleccionada, letra, guiones, contador)
        # En letra_en_palabra() incrementamos el contador

        if contador == 6:
            print(mostrar_ascii(contador))
            print(f"Has perdido. La palabra era: {palabra_seleccionada}")
            reanudar()

        elif "_" not in guiones:
            os.system("clear")
            print(mostrar_ascii(contador))
            print(f"Has adivinado la palabra {palabra_seleccionada}!")
            reanudar()


def main():
    juego()


if __name__ == '__main__':
    main()
