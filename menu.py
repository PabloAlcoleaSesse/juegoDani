from inicioJuego import Partida
import os

estadoMenu: bool = True


def menu(): 
    while True: 
        mostrarMenu()
        opcion = input("Selecciona una opción (1-4): ")
        gestionarOpcion(opcion)


def mostrarMenu():
    print ("=== Menú Principal ===")
    print ("1. Iniciar Juego")
    print ("2. Cargar Juego")
    print ("3. Historial de partidas")
    print ("4. Salir")


def gestionarOpcion(opcion):
    if opcion == '1':
        print("Iniciando nuevo juego...")

        os.system('cls' if os.name == 'nt' else 'clear')
        
        newPartida =  Partida("Jugador1")
        newPartida.iniciar_partida()
        opcion = False

    elif opcion == '2':
        print("Cargando juego...")
        # Lógica para cargar un juego existente
    elif opcion == '3':
        print("Mostrando historial de partidas...")
        # Lógica para mostrar el historial de partidas
    elif opcion == '4':
        print("Saliendo del juego. ¡Hasta luego!")
        estadoMenu = False
        exit()
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")




menu()

