import time

import habitaciones as hab
import herramientas as tools
import objetos as obj
import puzles as puz
from inventario import Inventario

PuertaCeldaAbierta = False
PuertaPatioAbierta = False
PanelReparado = False
SeguridadDesactivada = False


class Partida:
    def __init__(self, jugador1):
        self.jugador1 = jugador1
        self.habitacionActual = hab.celdaProtagonista
        self.inventario = Inventario()
        self.juegoActivo = True

    def iniciar_partida(self):
        flujoPrincipal(self, jugador=self.jugador1)

    def entrarEnHabitacion(self, habitacion):
        self.habitacionActual = habitacion
        self.habitacionActual.entrar()

    def procesarHabitacion(self):
        """Ejecuta las opciones de la habitación actual y retorna la siguiente habitación"""
        if self.habitacionActual == hab.celdaProtagonista:
            return opcionesCeldaProtagonista(self)
        elif self.habitacionActual == hab.pasilloDeCeldas:
            return opcionesPasilloDeCeldas(self)
        elif self.habitacionActual == hab.comedorPresos:
            return opcionesComedor(self)
        elif self.habitacionActual == hab.almacen:
            return opcionesAlmacen(self)
        elif self.habitacionActual == hab.salaControl:
            return opcionesSalaControl(self)
        elif self.habitacionActual == hab.patioExterior:
            return opcionesPatioExterior(self)
        elif self.habitacionActual == hab.tunelesSubterraneos:
            return opcionesTuneles(self)
        elif self.habitacionActual == hab.salidaFinal:
            return opcionesSalidaFinal(self)
        # Agregar más habitaciones aquí según sea necesario
        return None

    def cambiarHabitacion(self, nueva_habitacion):
        """Cambia a una nueva habitación"""
        if nueva_habitacion:
            self.habitacionActual = nueva_habitacion
            tools.pasarFase()
            self.habitacionActual.entrar()


def Bienvenida(nombreJugador):
    tools.clear()
    print(
        "Narrador: Despiertas en una celda oscura y fría, sin recordar cómo llegaste aquí."
    )
    time.sleep(2)
    print(
        "Narrador: Se escucha como golpea un objeto continuamente contra los barrotes de las cedas, cada vez se escucha mas ese sonido."
    )
    time.sleep(2)
    print("Guadia: Sea useted bienvenido a NOMBRE DE PRISION RANDOM")
    time.sleep(2)
    print(nombreJugador + ": Que hago aqui? Donde estoy?")
    time.sleep(2)
    print("Guadia: No me haga preguntas tontas y solo siga las reglas.")
    time.sleep(2)


def opcionesCeldaProtagonista(self):
    """Opciones de la celda del protagonista. Retorna la siguiente habitación o None."""
    global PuertaCeldaAbierta
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\nOpciones disponibles en la celda:")
        print("1. Comerse las gachas.")
        print("2. Examinar la cama.")
        print("3. Examinar la pared agrietada.")
        print("4. Revisar la pequeña estantería.")
        print("5. Intentar abrir la puerta de la celda.")
        print("6. Gritar pidiendo ayuda.")
        print("7. Ver inventario.")
        if PuertaCeldaAbierta:
            print("8. Salir de la celda.")

        try:
            opcion = int(input("Elige una opción (1-8): "))
            if opcion < 1 or opcion > 8:
                if opcion == 8 and not PuertaCeldaAbierta:
                    print("La puerta de la celda está cerrada. No puedes salir aún.")
                    continue
                raise ValueError("Número fuera de rango")

            ## Cuando el jugador come las gachas se encuentra una llave oxidada
            if opcion == 1:
                tools.clear()
                print(
                    "Decides comerte las gachas. No es la mejor comida, pero al menos te llena un poco."
                )
                time.sleep(2)
                print("Has mordido algo duro!!... es una llave!")
                time.sleep(1.5)
                self.inventario.añadirObjeto(obj.llaveOxidada)
                print("Has añadido una llave oxidada a tu inventario.")
                time.sleep(2)
                tools.pasarFase()

            # Examinar la cama
            elif opcion == 2:
                tools.clear()
                print(
                    "Has decidido examinar la cama. Está rota y sucia, no hay nada interesante aquí."
                )
                time.sleep(1.5)
                tools.pasarFase()

            # Examinar la pared agrietada
            elif opcion == 3:
                tools.clear()
                print(
                    "Examinas la pared agrietada, pero no encuentras nada fuera de lo común solo la via por donde escapa la felicidad de los presos."
                )
                time.sleep(2)
                tools.pasarFase()

            # Revisar la estantería
            elif opcion == 4:
                tools.clear()
                print("Se te ocurre revisar la estanteria, es alta y polvorienta.")
                time.sleep(2)
                print(
                    "Al fondo de la estanteria notas una pequeña bola de papel arrugada."
                )
                time.sleep(1)
                self.inventario.añadirObjeto(obj.nota)
                print("Has añadido una nota a tu inventario.")
                time.sleep(2)
                tools.pasarFase()

            # Intentar abrir la puerta de la celda
            elif opcion == 5:
                tools.clear()
                print("Intentas abrir la puerta de la celda.")
                time.sleep(1.5)
                if self.inventario.tieneObjeto(obj.llaveOxidada):
                    print("Usas la llave oxidada para abrir la puerta de la celda.")
                    time.sleep(2)
                    print("*CLICK*")
                    time.sleep(1)
                    PuertaCeldaAbierta = True
                    print("¡La puerta se abre! Ahora puedes salir.")
                    time.sleep(2)
                    tools.pasarFase()
                else:
                    print(
                        "La puerta está cerrada con llave. Necesitas encontrar una llave."
                    )
                    time.sleep(1.5)
                    tools.pasarFase()

            # Gritar pidiendo ayuda
            elif opcion == 6:
                tools.clear()
                print(
                    "Gritas pidiendo ayuda, pero nadie responde. Parece que estás solo aquí."
                )
                time.sleep(2)
                print("Solo escuchas el eco de tu propia voz...")
                time.sleep(1.5)
                tools.pasarFase()

            # Ver inventario
            elif opcion == 7:
                self.inventario.menu_inventario()

            # Salir de la celda
            elif opcion == 8 and PuertaCeldaAbierta:
                tools.clear()
                print("Sales de la celda y te adentras en el pasillo de la prisión.")
                time.sleep(2)
                EstadoMenu = False
                return hab.pasilloDeCeldas  # Retorna la siguiente habitación

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None  # Si no cambia de habitación


def opcionesPasilloDeCeldas(self):
    """Opciones del pasillo de celdas. Retorna la siguiente habitación o None."""
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\nOpciones disponibles en el pasillo de celdas:")
        print("1. Intentar abrir una celda cercana.")
        print("2. Examinar la caja metálica.")
        print("3. Intentar romper la camara de seguridad.")
        print("4. Acceder al comedor")
        print("5. Acceder al almacen.")
        print("6. Acceder a la sala de control.")
        print("7. Acceder a la celda donde despertaste.")
        print("8. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-8): "))
            if opcion < 1 or opcion > 8:
                raise ValueError("Número fuera de rango")

            # Intentar abrir celda cercana
            if opcion == 1:
                tools.clear()
                print("Intentas abrir una celda cercana, pero está cerrada con llave.")
                time.sleep(1.5)
                tools.pasarFase()

            # Examinar caja metálica
            elif opcion == 2:
                tools.clear()
                print("Examinas la caja metálica, tiene un candado numérico.")
                time.sleep(1.5)
                cajaAbierta = puz.puzleCandado()
                if cajaAbierta:
                    tools.clear()
                    print(
                        "Has abierto la caja metálica y encontrado una tarjeta magnética."
                    )
                    time.sleep(1)
                    self.inventario.añadirObjeto(obj.tarjetaMagnetica)
                    print("Has añadido una tarjeta magnética a tu inventario.")
                    time.sleep(2)
                    tools.pasarFase()
                else:
                    print("Decides no abrir la caja metálica por ahora.")
                    time.sleep(1)
                    tools.pasarFase()

            # Romper cámara
            elif opcion == 3:
                tools.clear()
                print("Intentas romper la cámara de seguridad, saltan chispas.")
                time.sleep(1)
                print("*CHISPAS* ¡Mejor no hacer eso!")
                time.sleep(1.5)
                tools.pasarFase()

            # Acceder al comedor
            elif opcion == 4:
                tools.clear()
                print("Intentas acceder al comedor")
                time.sleep(1.5)
                if self.inventario.tieneObjeto(obj.tarjetaMagnetica):
                    print("Usas la tarjeta magnética para acceder al comedor.")
                    time.sleep(1)
                    print("*BEEP* Acceso concedido.")
                    time.sleep(1.5)
                    EstadoMenu = False
                    return hab.comedorPresos  # Retorna la siguiente habitación
                else:
                    print(
                        "La puerta del comedor está cerrada con una tarjeta magnética. Necesitas una para entrar."
                    )
                    time.sleep(1.5)
                    tools.pasarFase()

            # Acceder al almacén
            elif opcion == 5:
                tools.clear()
                print("Esta cerrado con un candado.")
                time.sleep(1.5)
                if self.inventario.tieneObjeto(obj.destornillador):
                    print("Usas el destornillador para acceder al almacén.")
                    time.sleep(1)
                    print("*CLIC* La puerta se abre.")
                    time.sleep(1.5)
                    EstadoMenu = False
                    return hab.almacen  # Retorna la siguiente habitación
                else:
                    print(
                        "La puerta del almacén está atornillada. Necesitas un destornillador para entrar."
                    )
                    time.sleep(1.5)
                    tools.pasarFase()

            # Acceder a sala de control
            elif opcion == 6:
                tools.clear()
                print("Te acercas a la sala de control...")
                time.sleep(1.5)
                if self.inventario.tieneObjeto(obj.tarjetaSeguridadAvanzada):
                    print(
                        "Usas la tarjeta de seguridad avanzada para acceder a la sala de control."
                    )
                    time.sleep(1)
                    print("*BEEP BEEP* Acceso autorizado.")
                    time.sleep(1.5)
                    EstadoMenu = False
                    return hab.salaControl  # Retorna la siguiente habitación
                else:
                    print(
                        "La puerta de la sala de control está cerrada con una tarjeta de seguridad avanzada. Necesitas una para entrar."
                    )
                    time.sleep(1.5)
                    tools.pasarFase()

            # Volver a la celda
            elif opcion == 7:
                tools.clear()
                print("Regresas a la celda donde despertaste.")
                time.sleep(1)
                EstadoMenu = False
                return hab.celdaProtagonista  # Retorna la celda

            # Ver inventario
            elif opcion == 8:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número entre 1 y 8.")

    return None  # Si no cambia de habitación


def opcionesComedor(self):
    """Opciones del comedor. Retorna la siguiente habitación o None."""
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\nOpciones disponibles en el comedor:")
        print("1. Examinar las mesas.")
        print("2. Acercarte al policía .")
        print("3. Coger el pañuelo.")
        print("4. Examinar el tablon de anuncios.")
        print("5. Abrir puerta del patio exterior.")
        print("6. Revisar la maquina expendedora.")
        print("7. Volver al pasillo.")
        print("8. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-5): "))
            if opcion < 1 or opcion > 5:
                raise ValueError("Número fuera de rango")

            if opcion == 1:
                tools.clear()
                print("Examinas las mesas. Están sucias y llenas de restos de comida.")
                time.sleep(2)
                print("Encuentras una nota con un acertijo.")
                time.sleep(1)
                self.inventario.añadirObjeto(obj.notaAcertijo)
                print("Has añadido una nota con un acertijo a tu inventario.")
                time.sleep(2)
                tools.pasarFase()

            elif opcion == 2:
                tools.clear()
                print("Te acercas al policia dormido. Parece inofensivo.")
                time.sleep(1.5)
                print("Escuchas sus ronquidos. Está profundamente dormido.")
                time.sleep(1.5)
                tools.pasarFase()

            elif opcion == 3:
                tools.clear()
                print("Coges el pañuelo del suelo, parece que no tiene nada especial.")
                time.sleep(1.5)
                tools.pasarFase()

            elif opcion == 4:
                tools.clear()
                print(
                    "Lees los carteles absurdos en las paredes. Son reglas extrañas de la prisión."
                )
                time.sleep(2)
                print("Parece que hay una especie de cajon en el lateral del tablón.")
                time.sleep(2)
                print("Lo abres con cuidado...")
                time.sleep(1)
                self.inventario.añadirObjeto(obj.destornillador)
                print("Has añadido un destornillador a tu inventario.")
                print("Habia un destornillador en el cajon del tablón.")
                time.sleep(2)
                tools.pasarFase()

            elif opcion == 5:
                tools.clear()
                print("Intentas abrir la puerta del patio exterior.")
                time.sleep(1.5)
                if PuertaPatioAbierta:
                    print("La puerta ya está abierta, puedes salir al patio.")
                    time.sleep(2)
                    EstadoMenu = False
                    return hab.patioExterior
                else:
                    print(
                        "La puerta está cerrada. \n"
                        " Necesitas encontrar una forma de abrirla."
                    )
                    time.sleep(1.5)
                    tools.pasarFase()

            elif opcion == 6:
                tools.clear()
                print(
                    self.jugador1.nombre
                    + ": La verdad que un refresco carbonatado cuyo nombre no se puede decir porque no nos han pagado un solo duro me vendria bastante bien."
                )
                time.sleep(2)
                print("Revisas la máquina expendedora, pero está vacía y rota.")
                time.sleep(1)
                print("Te acuerdas que no tienes dinero, ")
                time.sleep(1.5)
                print("Estas en una prisión.")
                time.sleep(1)
                print("Lo tuyo nunca fue la lógica.")
                time.sleep(2)
                print("De la rabia decides meterle un puñetazo a la máquina.")
                time.sleep(1)
                print("PUM!")
                time.sleep(1.5)
                print("Sorpresa sorpresa, la máquina suelta un trozo de cable.")
                time.sleep(1)
                self.inventario.añadirObjeto(obj.trozoCable)
                print("Has añadido un trozo de cable a tu inventario.")
                time.sleep(2)
                print(
                    "No sabes para que puede servir un cable en una prisión, pero bueno, por si acaso."
                )
                time.sleep(2)
                tools.pasarFase()

            elif opcion == 7:
                tools.clear()
                print("Vuelves al pasillo de celdas.")
                time.sleep(1)
                EstadoMenu = False
                return hab.pasilloDeCeldas

            elif opcion == 5:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None


def opcionesAlmacen(self):
    """Opciones del almacén. Retorna la siguiente habitación o None."""
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\nOpciones disponibles en el almacén:")
        print(
            "1. Revisar los estantes, ya sabes, por si acaso. (Yo que tu lo haria (Nunca sabes que puedes encontrar escondido en los estantes (Quien avisa no es traido (De verdad no me vas a hacer caso (Vale ya paro)))))"
        )
        print("2. Examinar los mecanismos raros.")
        print("3. Volver al pasillo.")
        print("4. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-4): "))
            if opcion < 1 or opcion > 4:
                raise ValueError("Número fuera de rango")

            if opcion == 1:
                tools.clear()
                print("Empiezas a revisar los estantes.")
                time.sleep(2)
                print("Buscando...")
                time.sleep(2)
                print("Buscando...")
                time.sleep(2)
                print("Buscando...")
                time.sleep(2)
                print("Eureka! ")
                time.sleep(1)
                print("Lo has encontrado!")
                time.sleep(1)
                print("Polvo")
                time.sleep(1)
                print("Has encontrado polvo")
                time.sleep(2)
                print(
                    "Como dijo una vez Arthur Schopenhauer: \n"
                    "'No hay que confiar en nadie por completo. Si se observa con atención, se descubre que casi todos los hombres piensan primero en sí mismos y solo después, y solo si les conviene, en los demás.\n"
                    "La prudencia consiste en no esperar demasiado de nadie, porque quien deposita su confianza sin reservas se expone inevitablemente a la decepción. \n"
                    "Cuanto mejor se conoce al ser humano, más se comprende que la desconfianza no es maldad, sino una forma de lucidez.'"
                )
                time.sleep(3)
                print("\nY como me gusta decir a mi: \n")
                time.sleep(1)
                print("Espabila chaval")
                time.sleep(2)

                self.inventario.añadirObjeto(obj.polvo)
                print("Has añadido polvo a tu inventario.")
                time.sleep(1.5)
                tools.pasarFase()

            elif opcion == 2:
                tools.clear()
                print("Examinas los mecanismos raros. No entiendes para qué sirven.")
                time.sleep(1.5)
                puzleResuelto = puz.puzleInterruptores()
                if puzleResuelto:
                    tools.clear()
                    print("Se abre un compartimento secreto.")
                    time.sleep(1.5)
                    print("Has encontrado una tarjeta de seguridad avanzada.")
                    time.sleep(1)
                    self.inventario.añadirObjeto(obj.tarjetaSeguridadAvanzada)
                    print("Has encontrado una linterna.")
                    time.sleep(1)
                    self.inventario.añadirObjeto(obj.linterna)
                    time.sleep(1.5)
                    tools.pasarFase()

            elif opcion == 3:
                tools.clear()
                print("Vuelves al pasillo de celdas.")
                time.sleep(1)
                EstadoMenu = False
                return hab.pasilloDeCeldas
            elif opcion == 4:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None


def opcionesSalaControl(self):
    """Opciones de la sala de control. Retorna la siguiente habitación o None."""
    global PanelReparado, SeguridadDesactivada, PuertaPatioAbierta
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\nOpciones disponibles en la sala de control:")
        print("1. Examinar las cámaras de seguridad.")
        print("2. Leer documentos sospechosos.")
        print("3. Revisar el suelo.")
        print("4. Reparar el panel eléctrico.")
        print("5. Desactivar seguridad del patio.")
        print("6. Matar al policía.")
        print("7. Interrogar al policía.")
        print("8. Volver al pasillo.")
        print("9. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-9): "))
            if opcion < 1 or opcion > 9:
                raise ValueError("Número fuera de rango")

            if opcion == 1:
                tools.clear()
                print(
                    "Examinas las pantallas de seguridad. Muestran diferentes áreas de la prisión."
                )
                time.sleep(2)
                print("Ves cámaras en: Celda, Pasillo, Comedor y Patio.")
                time.sleep(2)

            elif opcion == 2:
                tools.clear()
                print("Revisas los documentos en un escritorio...")
                time.sleep(2)
                print("Encuentras un documento interesante.")
                self.inventario.añadirObjeto(obj.documentoSecreto)
                print("Has añadido un documento secreto a tu inventario.")
                time.sleep(2)
                print(
                    "El documento menciona algo sobre 'el orden en que caen los presos'..."
                )
                time.sleep(2)

            elif opcion == 3:
                tools.clear()
                print("Revisas el suelo buscando algo útil.")
                time.sleep(2)
                print("En una esquina encuentras un mapa hecho una bola.")
                self.inventario.añadirObjeto(obj.mapaAntiguo)
                print("Has añadido un mapa antiguo de túneles a tu inventario.")
                print("Está parcialmente roto pero podría ser útil.")
                time.sleep(2)

            elif opcion == 4:
                tools.clear()
                print("Te acercas al panel eléctrico. Está dañado y chisporrotea.")
                time.sleep(1)
                if PanelReparado:
                    print("El panel ya está reparado y funcionando correctamente.")
                else:
                    # Verificar si tiene los objetos necesarios
                    if (
                        self.inventario.tieneObjeto(obj.trozoCable)
                        and self.inventario.tieneObjeto(obj.destornillador)
                        and self.inventario.tieneObjeto(obj.tarjetaMagnetica)
                    ):
                        print("\nTienes todo lo necesario para reparar el panel:")
                        print("✓ Trozo de cable")
                        print("✓ Destornillador")
                        print("✓ Tarjeta magnética")
                        time.sleep(2)

                        puz.puzlePanel()

                        print("\nComienzas a trabajar en el panel...")
                        time.sleep(2)
                        print("Usas el destornillador para abrir el panel.")
                        time.sleep(2)
                        print("Conectas el trozo de cable a los circuitos dañados.")
                        time.sleep(2)
                        print("Insertas la tarjeta magnética en el lector.")
                        time.sleep(2)
                        print("\n¡BZZZZT!")
                        print("El panel cobra vida. Las luces se encienden.")
                        print("¡Panel reparado exitosamente!")
                        PanelReparado = True
                    else:
                        print("El panel está muy dañado. Necesitas:")
                        if not self.inventario.tieneObjeto(obj.trozoCable):
                            print("- Un cable para reconectar circuitos")
                        if not self.inventario.tieneObjeto(obj.destornillador):
                            print("- Un destornillador para asegurar conexiones")
                        if not self.inventario.tieneObjeto(obj.tarjetaMagnetica):
                            print("- Una tarjeta magnética para activar el sistema")

            elif opcion == 5:
                tools.clear()
                print("Intentas desactivar el sistema de seguridad del patio.")
                time.sleep(1)
                if not PanelReparado:
                    print("El panel eléctrico no funciona. Debes repararlo primero.")
                elif SeguridadDesactivada:
                    print("La seguridad del patio ya está desactivada.")
                else:
                    # Ejecutar el puzzle de cámaras
                    if puz.puzleCamaras():
                        tools.clear()
                        SeguridadDesactivada = True
                        PuertaPatioAbierta = True
                        print("\n¡SISTEMA DE SEGURIDAD DESACTIVADO!")
                        print("La puerta del patio exterior está ahora desbloqueada.")
                        time.sleep(3)
                    else:
                        print("No lograste desactivar el sistema correctamente.")
                        time.sleep(1)

            elif opcion == 6:
                tools.clear()
                print("Te acercas sigilosamente al policía dormido...")
                time.sleep(2)
                print(
                    self.jugador1.nombre + ": No puedo hacer esto. No soy un asesino."
                )
                print("Decides buscar otra forma de escapar.")
                time.sleep(2)

            elif opcion == 7:
                tools.clear()
                print("Decides despertar al policía para interrogarlo.")
                time.sleep(2)
                print("Policía: ¿QUÉ? ¿QUIÉN ANDA AHÍ?")
                time.sleep(2)
                print("¡ALARMA! ¡ALARMA! ¡PRISIONERO ESCAPADO!")
                time.sleep(2)
                tools.clear()
                print("\n=== GAME OVER ===")
                print("Los guardias te capturan y te llevan de vuelta a tu celda.")
                print("Tu intento de escape ha fracasado.")
                time.sleep(3)
                print("\nReiniciando el juego...")
                time.sleep(2)
                # Reiniciar el juego
                EstadoMenu = False
                return hab.celdaProtagonista

            elif opcion == 8:
                tools.clear()
                print("Vuelves al pasillo de celdas.")
                time.sleep(1)
                EstadoMenu = False
                return hab.pasilloDeCeldas

            elif opcion == 9:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None


def opcionesPatioExterior(self):
    """Opciones del patio exterior. Retorna la siguiente habitación o None."""
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\nOpciones disponibles en el patio exterior:")
        print("1. Dar una vuelta por el patio.")
        print("2. Hacer deporte en el gimnasio exterior.")
        print("3. Intentar abrir la trampilla metálica.")
        print("4. Leer marcas en el suelo.")
        print("5. Buscar debajo de los bancos.")
        print("6. Usar linterna en zonas oscuras.")
        print("7. Volver al comedor.")
        print("8. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-8): "))
            if opcion < 1 or opcion > 8:
                raise ValueError("Número fuera de rango")

            if opcion == 1:
                tools.clear()
                print(
                    "Das una vuelta por el patio. El aire fresco se siente bien después de tanto tiempo encerrado."
                )
                time.sleep(2)
                print("Ves el cielo nocturno por primera vez en mucho tiempo.")
                print("Las estrellas brillan intensamente.")
                time.sleep(2)

            elif opcion == 2:
                tools.clear()
                print(
                    self.jugador1.nombre
                    + ": Mmm, quizás debería hacer algo de ejercicio..."
                )
                time.sleep(2)
                print("Haces algunas flexiones y sentadillas.")
                print(
                    "Te sientes un poco más fuerte, pero no es momento para entrenar."
                )
                time.sleep(2)

            elif opcion == 3:
                tools.clear()
                print("Examinas la trampilla metálica en el suelo.")
                time.sleep(1)
                if self.inventario.tieneObjeto(obj.tarjetaSeguridadAvanzada):
                    print(
                        "Usas la tarjeta de seguridad avanzada en el lector de la trampilla."
                    )
                    time.sleep(2)
                    print("¡CLIC! La trampilla se desbloquea.")
                    print("Puedes ver unas escaleras que descienden a la oscuridad.")
                    time.sleep(2)
                    print("Bajas por las escaleras hacia los túneles subterráneos...")
                    time.sleep(2)
                    EstadoMenu = False
                    return hab.tunelesSubterraneos
                else:
                    print("La trampilla tiene una cerradura electrónica.")
                    print(
                        "Necesitas una tarjeta de seguridad de alto nivel para abrirla."
                    )
                    time.sleep(1)

            elif opcion == 4:
                tools.clear()
                print("Examinas las marcas extrañas en el suelo del patio.")
                time.sleep(2)
                print("Parecen ser grabados hechos por antiguos prisioneros.")
                print("Algunas marcas forman flechas que apuntan hacia la trampilla.")
                time.sleep(2)

            elif opcion == 5:
                tools.clear()
                print("Revisas debajo de los bancos del patio.")
                time.sleep(2)
                print("No encuentras nada útil, solo basura y oxidación.")
                time.sleep(1)

            elif opcion == 6:
                tools.clear()
                if self.inventario.tieneObjeto(obj.linterna):
                    print("Usas la linterna para iluminar las zonas oscuras del patio.")
                    time.sleep(2)
                    print(
                        "La luz revela algunos rincones ocultos, pero no hay nada importante aquí."
                    )
                    time.sleep(1)
                else:
                    print("No tienes una linterna para iluminar la oscuridad.")
                    time.sleep(1)

            elif opcion == 7:
                tools.clear()
                print("Vuelves al comedor de presos.")
                time.sleep(1)
                EstadoMenu = False
                return hab.comedorPresos

            elif opcion == 8:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None


def opcionesTuneles(self):
    """Opciones de los túneles subterráneos. Retorna la siguiente habitación o None."""
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\n" + "=" * 50)
        print("TÚNELES SUBTERRÁNEOS")
        print("=" * 50)
        print("\nEstás en un lugar oscuro y húmedo.")
        print("El eco de las gotas de agua resuena en las paredes.")

        print("\nOpciones disponibles:")
        print("1. Usar la linterna.")
        print("2. Analizar el mapa roto.")
        print("3. Intentar navegar por los túneles.")
        print("4. Volver al patio exterior.")
        print("5. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-5): "))
            if opcion < 1 or opcion > 5:
                raise ValueError("Número fuera de rango")

            if opcion == 1:
                tools.clear()
                if self.inventario.tieneObjeto(obj.linterna):
                    print("Enciendes la linterna. La luz ilumina los túneles oscuros.")
                    time.sleep(2)
                    print(
                        "Ves varios caminos que se bifurcan en diferentes direcciones."
                    )
                    print("Sin el mapa, sería imposible saber qué camino tomar.")
                    time.sleep(2)
                else:
                    print("No tienes una linterna. La oscuridad es total.")
                    print("Sería peligroso avanzar sin luz.")
                    time.sleep(1)

            elif opcion == 2:
                tools.clear()
                if self.inventario.tieneObjeto(obj.mapaAntiguo):
                    print("Despliegas el mapa antiguo y lo examinas con cuidado.")
                    time.sleep(2)
                    print("Aunque está parcialmente roto, puedes ver algunas pistas:")
                    print("- Una flecha dibujada apuntando a la izquierda")
                    print("- Gotas de agua dibujadas señalando recto")
                    print("- Marcas en círculo con una flecha a la derecha")
                    time.sleep(2)
                    print("Este mapa te ayudará a navegar por los túneles.")
                    time.sleep(2)
                else:
                    print("No tienes ningún mapa. Estarías perdido sin uno.")
                    time.sleep(1)

            elif opcion == 3:
                # Verificar que tenga linterna y mapa
                tools.clear()
                if not self.inventario.tieneObjeto(obj.linterna):
                    print("No puedes navegar sin luz. Necesitas una linterna.")
                    time.sleep(1)
                elif not self.inventario.tieneObjeto(obj.mapaAntiguo):
                    print(
                        "Sin un mapa, te perderías en los túneles. Es demasiado peligroso."
                    )
                    time.sleep(1)
                else:
                    print(
                        "\nTienes todo lo necesario para intentar cruzar los túneles."
                    )
                    time.sleep(2)

                    if puz.puzleOrientacion():
                        tools.clear()
                        print("\n¡Has llegado al final de los túneles!")
                        time.sleep(2)
                        print("Frente a ti ves una puerta metálica imponente.")
                        print("Esta debe ser la salida...")
                        time.sleep(2)
                        EstadoMenu = False
                        return hab.salidaFinal
                    else:
                        print("\nTe has perdido en los túneles y vuelves al inicio.")
                        print("Debes intentarlo de nuevo, pero con más cuidado.")
                        time.sleep(2)

            elif opcion == 4:
                tools.clear()
                print("Subes de vuelta al patio exterior.")
                time.sleep(1)
                EstadoMenu = False
                return hab.patioExterior

            elif opcion == 5:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None


def opcionesSalidaFinal(self):
    """Opciones de la salida final. Retorna None (fin del juego)."""
    EstadoMenu = True

    while EstadoMenu:
        tools.clear()
        print("\n" + "=" * 60)
        print("                    SALIDA FINAL")
        print("=" * 60)
        print("\nFrente a ti hay una puerta metálica antigua y blindada.")
        print("Esta es tu última oportunidad de escapar...")

        print("\nOpciones disponibles:")
        print("1. Examinar la puerta.")
        print("2. Intentar abrir la puerta.")
        print("3. Revisar el marco de la puerta.")
        print("4. Volver a los túneles.")
        print("5. Ver inventario.")

        try:
            opcion = int(input("Elige una opción (1-5): "))
            if opcion < 1 or opcion > 5:
                raise ValueError("Número fuera de rango")

            if opcion == 1:
                tools.clear()
                print("\nExaminas la puerta detenidamente.")
                time.sleep(2)
                print("Tiene tres mecanismos de seguridad:")
                print("1. Un lector de tarjetas de seguridad")
                print("2. Un teclado numérico para ingresar un código")
                print("3. Un panel de acceso que parece necesitar herramientas")
                time.sleep(2)
                print("\nNecesitarás superar los tres mecanismos para abrir la puerta.")
                time.sleep(2)

            elif opcion == 2:
                tools.clear()
                print("\nIntentas abrir la puerta de escape...")
                time.sleep(2)

                puz.puzleSalidaFinal()

                # Verificar Mecanismo 1: Tarjeta de seguridad avanzada
                print("\n--- MECANISMO 1: LECTOR DE TARJETAS ---")
                if self.inventario.tieneObjeto(obj.tarjetaSeguridadAvanzada):
                    print("Insertas la tarjeta de seguridad avanzada.")
                    time.sleep(2)
                    print("¡BEEP! Luz verde. Primer mecanismo desbloqueado.")
                    mecanismo1 = True
                else:
                    print("No tienes una tarjeta de seguridad avanzada.")
                    print("No puedes abrir esta puerta sin ella.")
                    mecanismo1 = False
                    continue

                time.sleep(2)

                # Verificar Mecanismo 2: Código numérico
                print("\n--- MECANISMO 2: TECLADO NUMÉRICO ---")
                print("Necesitas ingresar un código de 3 dígitos.")

                if self.inventario.tieneObjeto(obj.documentoSecreto):
                    print(
                        "Recuerdas el documento que encontraste en la sala de control."
                    )
                    print("Mencionaba el código: 314")

                codigo = input("Ingresa el código: ")
                if codigo == "314":
                    print("¡BEEP! ¡BEEP! Luz verde. Segundo mecanismo desbloqueado.")
                    mecanismo2 = True
                else:
                    print("Código incorrecto. La puerta permanece cerrada.")
                    mecanismo2 = False
                    continue

                time.sleep(2)

                # Verificar Mecanismo 3: Panel manual con herramientas
                print("\n--- MECANISMO 3: PANEL DE ACCESO MANUAL ---")
                print("Hay un panel que debe ser ajustado manualmente.")

                if self.inventario.tieneObjeto(obj.destornillador):
                    print("Usas el destornillador para ajustar el mecanismo interno.")
                    time.sleep(2)
                    print("¡CLIC! El mecanismo se ajusta correctamente.")
                    print("Tercer mecanismo desbloqueado.")
                    mecanismo3 = True
                else:
                    print("Necesitas una herramienta para ajustar este mecanismo.")
                    print("Un destornillador funcionaría perfectamente.")
                    mecanismo3 = False
                    continue

                time.sleep(2)

                # Si todos los mecanismos están desbloqueados
                if mecanismo1 and mecanismo2 and mecanismo3:
                    tools.clear()
                    print("\n" + "=" * 60)
                    print("                ¡TODOS LOS MECANISMOS DESBLOQUEADOS!")
                    print("=" * 60)
                    time.sleep(2)
                    print("\nLa puerta emite un sonido profundo...")
                    time.sleep(2)
                    print("CLANK... CLANK... CLANK...")
                    time.sleep(2)
                    print("\nLos cerrojos se abren uno por uno.")
                    time.sleep(2)
                    print("\nLa puerta comienza a abrirse lentamente...")
                    time.sleep(3)
                    print("\n¡LA PUERTA ESTÁ ABIERTA!")
                    time.sleep(2)

                    # Final del juego
                    print("\n" + "=" * 60)
                    print("                    ¡HAS ESCAPADO!")
                    print("=" * 60)
                    time.sleep(2)
                    print(
                        f"\n{self.jugador1.nombre}, sales por la puerta hacia la libertad."
                    )
                    time.sleep(2)
                    print("El aire fresco de la noche llena tus pulmones.")
                    time.sleep(2)
                    print("Corres hacia el bosque cercano sin mirar atrás.")
                    time.sleep(3)
                    print(
                        "\nPero mientras te alejas, encuentras una nota en el suelo..."
                    )
                    time.sleep(2)
                    print("\nLa nota dice:")
                    print('"No todos los que escaparon lo hicieron libres..."')
                    time.sleep(3)
                    print("\n¿Qué significa esto?")
                    time.sleep(2)
                    print("¿Realmente eras inocente?")
                    time.sleep(2)
                    print("¿O había una razón para que estuvieras allí?")
                    time.sleep(3)
                    print("\n" + "=" * 60)
                    print("                    FIN DEL JUEGO")
                    print("=" * 60)
                    print("\n¡Gracias por jugar!")
                    print("Desarrollado para Dani")
                    time.sleep(3)

                    # Terminar el juego
                    self.juegoActivo = False
                    EstadoMenu = False
                    return None

            elif opcion == 3:
                tools.clear()
                print("Revisas el marco de la puerta buscando pistas.")
                time.sleep(2)
                print("Hay marcas de desgaste y rayones antiguos.")
                print("Otros prisioneros intentaron escapar por aquí antes...")
                time.sleep(2)

            elif opcion == 4:
                tools.clear()
                print("Decides volver a los túneles por si olvidaste algo.")
                time.sleep(1)
                EstadoMenu = False
                return hab.tunelesSubterraneos

            elif opcion == 5:
                self.inventario.menu_inventario()

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número válido.")

    return None


def flujoPrincipal(self, jugador):
    """Bucle principal del juego con sistema de navegación centralizado"""
    tools.clear()
    print("\n" + "=" * 60)
    print(f"       Partida iniciada para {jugador.nombre}")
    print("=" * 60)
    time.sleep(2)
    tools.pasarFase()
    Bienvenida(jugador.nombre)
    tools.pasarFase()
    self.habitacionActual.entrar()

    # Bucle principal - evita recursión infinita
    while self.juegoActivo:
        nueva_habitacion = self.procesarHabitacion()

        if nueva_habitacion:
            self.cambiarHabitacion(nueva_habitacion)
        # Si no hay nueva habitación, continúa en la actual

    # Cuando el juego termina
    print("\n¡Partida finalizada!")
    input("\nPresiona ENTER para volver al menú principal...")
