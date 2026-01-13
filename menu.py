import os
import time

import herramientas as tools
from inicioJuego import Partida

estadoMenu: bool = True


def menu(jugador):
    while estadoMenu:
        tools.clear()
        mostrarMenu()
        opcion = input("Selecciona una opción (1-4): ")
        gestionarOpcion(opcion, jugador)


def mostrarMenu():
    print("\n" + "=" * 50)
    print("       PRISIÓN ESCAPE - MENÚ PRINCIPAL")
    print("=" * 50)
    print("\n1. Iniciar Juego")
    print("2. Salir")
    print("\n" + "=" * 50)


def gestionarOpcion(opcion, jugador):
    global estadoMenu

    if opcion == "1":
        tools.clear()
        print("Iniciando nuevo juego...")
        time.sleep(1)
        print("Cargando partida...")
        time.sleep(1)
        tools.clear()

        partida = Partida(jugador)
        partida.iniciar_partida()
        estadoMenu = False
    elif opcion == "2":
        tools.clear()
        print("\n" + "=" * 50)
        print("Saliendo del juego...")
        time.sleep(1)
        print("¡Hasta luego, " + jugador.nombre + "!")
        print("=" * 50 + "\n")
        time.sleep(1)
        estadoMenu = False
        exit()
    else:
        print("\nOpción no válida. Por favor, elige una opción del 1 al 2.")
        time.sleep(1.5)
