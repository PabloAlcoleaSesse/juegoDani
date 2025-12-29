from symtable import Function
from jugador import Jugador
import menu
from parser import getNombreJugador, guardarNombreJugador


def main(): 
    try: 
        jugador = Jugador(getNombreJugador())
        if jugador.nombre == None or jugador.nombre == "":
            print("Introduce el nombre del jugador")
            nombreJugador = input("Nombre del jugador: ")
            jugador.nombre = nombreJugador
            guardarNombreJugador(jugador.nombre)
        menu.menu(jugador)
    except KeyboardInterrupt:
        print("\nSaliendo del juego. ¡Hasta luego!")
        exit()


    
main()