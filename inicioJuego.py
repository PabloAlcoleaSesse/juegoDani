import time
import herramientas as tools


import habitaciones as hab


class Partida: 
    def __init__(self, jugador1):
        self.jugador1 = jugador1
        self.habitacionActual = hab.celdaProtagonista
        self.Inventario = []
    
    def iniciar_partida(self):
        flujoPrincipal(self, jugador=self.jugador1)

    def entrarEnHabitacion(self, habitacion):
        self.habitacionActual = habitacion
        self.habitacionActual.entrar()


def Bienvenida(nombreJugador): 

    tools.clear()

    print("Narrador: Despiertas en una celda oscura y fría, sin recordar cómo llegaste aquí.")
    time.sleep(2)
    print("Narrador: Se escucha como golpea un objeto continuamente contra los barrotes de las cedas, cada vez se escucha mas ese sonido.")
    time.sleep(2)
    print("Guadia: Sea useted bienvenido a NOMBRE DE PRISION RANDOM")
    time.sleep(2) 
    print( nombreJugador + ": Que hago aqui? Donde estoy?")
    time.sleep(2)
    print("Guadia: No me haga preguntas tontas y solo siga las reglas.")
    time.sleep(2)



def flujoPrincipal(self, jugador): 
        print(f"Partida iniciada para {jugador.nombre}")
        tools.pasarFase()
        Bienvenida(jugador.nombre)
        tools.pasarFase()
        time.sleep(3)
        self.habitacionActual.entrar()
        # Primera parte del juego, introducción, etc.



        
        








