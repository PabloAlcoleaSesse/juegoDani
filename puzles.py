import time

import herramientas as tools


def puzleCandado():
    """Puzzle del candado numérico en la caja metálica del pasillo"""
    estadoPuzle = True
    while estadoPuzle:
        tools.clear()
        print("\n=== CANDADO NUMÉRICO ===")
        time.sleep(1)
        print(
            "Para abrir el candado numérico, debes ingresar el código correcto de 4 dígitos."
        )
        time.sleep(1)
        print("Pista: Recuerda la nota que encontraste... (S,R,T,O)")
        time.sleep(1)
        print("\n1. Resolver candado")
        print("2. Salir")
        try:
            eleccion = input("\nElige una opción (1-2): ")
            if eleccion != "1" and eleccion != "2":
                raise ValueError("Número fuera de rango")
            if eleccion == "2":
                estadoPuzle = False
                print("\nDecides no intentar abrir el candado por ahora.")
                time.sleep(1.5)
                tools.pasarFase()
                return False
            print("\nExaminas el candado con atención...")
            time.sleep(1.5)
            codigoIngresado = input("Ingresa el código de 4 dígitos: ")
            print("\nProbando código...")
            time.sleep(1.5)
            # S=8, R=7, T=5, O=5 basado en las letras mayúsculas de la nota
            if codigoIngresado == "8755":
                tools.clear()
                print("\n¡CLICK! ¡CLICK! ¡CLICK!")
                time.sleep(1)
                print("Has ingresado el código correcto. El candado se abre.")
                time.sleep(2)
                estadoPuzle = False
                return True
            else:
                print("\n*BEEP* Código incorrecto. El candado sigue cerrado.")
                time.sleep(1.5)
                print("¿Hay alguna pista que hayas pasado por alto?")
                time.sleep(2)
                tools.pasarFase()

        except ValueError as e:
            print(f"\nEntrada inválida: {e}. Por favor, elige un número entre 1 y 2.")
            time.sleep(1.5)
            continue


def puzleInterruptores():
    """Puzzle de secuencia de interruptores en el almacén"""
    tools.clear()
    print("\n" + "=" * 50)
    print("           PANEL DE INTERRUPTORES")
    print("=" * 50)
    time.sleep(1)
    print("\nVes un panel con 5 interruptores numerados del 1 al 5.")
    time.sleep(1.5)
    print("Parece que deben activarse en un orden específico...")
    time.sleep(2)
    print(
        "\nRecuerdas la nota del comedor: 'El orden no es numérico, es el del castigo.'"
    )
    time.sleep(2)
    print("En la pared ves marcas extrañas: III - I - V")
    time.sleep(2)

    estadoPuzle = True
    intentos = 0
    max_intentos = 3

    while estadoPuzle and intentos < max_intentos:
        print(f"\n[Intento {intentos + 1}/{max_intentos}]")
        print("Debes activar 3 interruptores en el orden correcto.")
        time.sleep(1)
        print("Interruptores disponibles: 1, 2, 3, 4, 5")
        print("\n¿Intentar resolver el puzzle? (s/n): ", end="")

        respuesta = input().lower()
        if respuesta != "s":
            print("\nDecides dejarlo para después.")
            time.sleep(1.5)
            tools.pasarFase()
            return False

        print("\nMuy bien, vamos a intentarlo...")
        time.sleep(1)
        secuencia = []
        for i in range(3):
            try:
                interruptor = input(f"Interruptor {i + 1}: ")
                secuencia.append(interruptor)
                print("*CLIC*")
                time.sleep(0.5)
            except:
                print("Entrada inválida.")
                time.sleep(1)
                intentos += 1
                continue

        print("\nVerificando secuencia...")
        time.sleep(2)
        # Solución: 3, 1, 5 (basado en las marcas III=3, I=1, V=5)
        if secuencia == ["3", "1", "5"]:
            tools.clear()
            print("\n¡CLIC! ¡CLIC! ¡CLIC!")
            time.sleep(1)
            print("Los interruptores se iluminan en verde.")
            time.sleep(1.5)
            print("Escuchas un sonido mecánico detrás de las cajas...")
            time.sleep(2)
            print("\n¡Un compartimento secreto se ha abierto!")
            time.sleep(2)
            return True
        else:
            intentos += 1
            print("\n*BZZZZT* Nada sucede. Esa no es la secuencia correcta.")
            time.sleep(1.5)
            if intentos < max_intentos:
                print("Las marcas en la pared deben significar algo...")
                time.sleep(2)
                tools.pasarFase()

    print("\nDemasiados intentos fallidos. El panel se bloquea temporalmente.")
    time.sleep(2)
    tools.pasarFase()
    return False


def puzlePanel():
    """Puzzle para reparar el panel eléctrico en la sala de control"""
    tools.clear()
    print("\n" + "=" * 50)
    print("           PANEL ELÉCTRICO")
    print("=" * 50)
    time.sleep(1)
    print("\nEl panel está dañado. Los cables cuelgan y chisporrotean.")
    time.sleep(1.5)
    print("*BZZZZT* *CHISPA* *BZZZZT*")
    time.sleep(1)
    print("Necesitas repararlo para restaurar el sistema.")
    time.sleep(2)

    print("\nParece que necesitas:")
    time.sleep(1)
    print("- Un cable para reconectar los circuitos")
    time.sleep(0.5)
    print("- Un destornillador para asegurar las conexiones")
    time.sleep(0.5)
    print("- Una tarjeta magnética para activar el sistema")
    time.sleep(2)

    return True  # Se verifica en la función que llama si tiene los objetos


def puzleCamaras():
    """Puzzle de desactivar las cámaras en el orden correcto"""
    tools.clear()
    print("\n" + "=" * 50)
    print("           SISTEMA DE SEGURIDAD")
    print("=" * 50)
    time.sleep(1)
    print("\nVes 4 monitores mostrando diferentes áreas de la prisión:")
    time.sleep(1)
    print("1. Celda")
    time.sleep(0.5)
    print("2. Pasillo")
    time.sleep(0.5)
    print("3. Comedor")
    time.sleep(0.5)
    print("4. Patio")
    time.sleep(2)

    print("\nRecuerdas el documento que encontraste:")
    time.sleep(1)
    print("'Las cámaras miran en el mismo orden en el que caen los presos.'")
    time.sleep(2)
    print("\nDebes desactivar las cámaras en el orden correcto.")
    time.sleep(2)

    estadoPuzle = True
    intentos = 0
    max_intentos = 2

    while estadoPuzle and intentos < max_intentos:
        print(f"\n[Intento {intentos + 1}/{max_intentos}]")
        print("Ingresa el orden para desactivar las 4 cámaras:")
        time.sleep(1)

        try:
            cam1 = input("Cámara 1: ")
            cam2 = input("Cámara 2: ")
            cam3 = input("Cámara 3: ")
            cam4 = input("Cámara 4: ")

            print("\nProcesando secuencia...")
            time.sleep(2)
            # Orden correcto: Celda(1), Pasillo(2), Patio(4), Túneles (pero no hay túneles en la lista, así que es Comedor)
            # El orden lógico de la prisión es: Celda -> Pasillo -> Patio
            # Pero según el documento original: Celda, Pasillo, Patio, Túneles
            # Como solo hay 4 opciones, el orden es: 1, 2, 4, 3
            if [cam1, cam2, cam3, cam4] == ["1", "2", "4", "3"]:
                tools.clear()
                print("\n" + "=" * 50)
                print("¡SISTEMA DESACTIVADO!")
                print("=" * 50)
                time.sleep(1.5)
                print("\nLas luces rojas de las cámaras se apagan una por una.")
                time.sleep(1)
                print("*BEEP* Cámara 1... desactivada")
                time.sleep(0.8)
                print("*BEEP* Cámara 2... desactivada")
                time.sleep(0.8)
                print("*BEEP* Cámara 3... desactivada")
                time.sleep(0.8)
                print("*BEEP* Cámara 4... desactivada")
                time.sleep(1.5)
                print("\n¡La seguridad del patio exterior ha sido desactivada!")
                time.sleep(2)
                return True
            else:
                intentos += 1
                print("\n*WEEEE-OOOO-WEEEE* ¡ALARMA! Las luces parpadean.")
                time.sleep(1.5)
                print("Esa no es la secuencia correcta.")
                time.sleep(1.5)
                if intentos < max_intentos:
                    print("Piensa en el recorrido natural de un prisionero...")
                    time.sleep(2)
                    tools.pasarFase()

        except:
            intentos += 1
            print("\nEntrada inválida.")
            time.sleep(1)

    print("\nEl sistema se bloquea. No puedes intentarlo de nuevo ahora.")
    time.sleep(2)
    tools.pasarFase()
    return False


def puzleOrientacion():
    """Puzzle de navegación en los túneles subterráneos"""
    tools.clear()
    print("\n" + "=" * 50)
    print("           TÚNELES SUBTERRÁNEOS")
    print("=" * 50)
    time.sleep(1)
    print("\nEstás en un laberinto oscuro. Tu linterna ilumina el camino.")
    time.sleep(1.5)
    print("Tienes el mapa roto. Intentas descifrar las marcas...")
    time.sleep(2)

    print("\nEn el mapa ves:")
    time.sleep(1)
    print("- Una flecha dibujada apuntando a la izquierda")
    time.sleep(0.8)
    print("- Gotas de agua señalando hacia adelante")
    time.sleep(0.8)
    print("- Marcas en círculo con una flecha a la derecha")
    time.sleep(2)

    camino = []

    print("\n--- PRIMERA ENCRUCIJADA ---")
    time.sleep(1)
    print("El túnel se divide en tres direcciones.")
    time.sleep(1)
    print("1. Izquierda (paredes húmedas)")
    time.sleep(0.5)
    print("2. Recto (sonido de agua goteando)")
    time.sleep(0.5)
    print("3. Derecha (olor a moho)")
    time.sleep(1)

    eleccion1 = input("\n¿Qué camino tomas? (1/2/3): ")
    camino.append(eleccion1)

    print("\nCaminas con cuidado...")
    time.sleep(1.5)
    if eleccion1 != "1":
        print("Caminas durante un rato y llegas a un callejón sin salida.")
        time.sleep(2)
        print("Debes volver al inicio.")
        time.sleep(2)
        tools.pasarFase()
        return False

    print("Avanzas por el túnel de la izquierda...")
    time.sleep(2)

    print("\n--- SEGUNDA ENCRUCIJADA ---")
    time.sleep(1)
    print("Otra división del camino.")
    time.sleep(1)
    print("1. Izquierda (muy oscuro)")
    time.sleep(0.5)
    print("2. Recto (escuchas gotas de agua)")
    time.sleep(0.5)
    print("3. Derecha (corriente de aire)")
    time.sleep(1)

    eleccion2 = input("\n¿Qué camino tomas? (1/2/3): ")
    camino.append(eleccion2)

    print("\nAvanzas con la linterna en alto...")
    time.sleep(1.5)
    if eleccion2 != "2":
        print("El camino se vuelve más estrecho hasta que no puedes continuar.")
        time.sleep(2)
        print("Debes retroceder al inicio.")
        time.sleep(2)
        tools.pasarFase()
        return False

    print("Sigues recto, las gotas de agua te guían...")
    time.sleep(2)

    print("\n--- TERCERA ENCRUCIJADA ---")
    time.sleep(1)
    print("La última división.")
    time.sleep(1)
    print("1. Izquierda (completamente oscuro)")
    time.sleep(0.5)
    print("2. Recto (paredes cerradas)")
    time.sleep(0.5)
    print("3. Derecha (ves una luz tenue a lo lejos)")
    time.sleep(1)

    eleccion3 = input("\n¿Qué camino tomas? (1/2/3): ")
    camino.append(eleccion3)

    print("\nDas el último paso...")
    time.sleep(1.5)
    if eleccion3 != "3":
        print("Te encuentras con una pared de roca sólida.")
        time.sleep(2)
        print("Este no es el camino. Vuelves al inicio.")
        time.sleep(2)
        tools.pasarFase()
        return False

    tools.clear()
    print("\n" + "=" * 50)
    print("¡Lo lograste!")
    print("=" * 50)
    time.sleep(1.5)
    print("\nLa luz se hace más brillante a medida que avanzas.")
    time.sleep(1.5)
    print("Has navegado exitosamente por los túneles.")
    time.sleep(2)
    return True


def puzleSalidaFinal():
    """Puzzle final de la salida que combina múltiples elementos"""
    tools.clear()
    print("\n" + "=" * 60)
    print("                    SALIDA FINAL")
    print("=" * 60)
    time.sleep(1)
    print("\nFrente a ti hay una puerta metálica antigua.")
    time.sleep(1.5)
    print("Tiene tres mecanismos de seguridad:")
    time.sleep(2)

    print("\n1. Un lector de tarjetas de seguridad")
    time.sleep(0.8)
    print("2. Un teclado numérico")
    time.sleep(0.8)
    print("3. Un panel de acceso que requiere herramientas")
    time.sleep(2)

    print("\nEsta es tu última oportunidad de escapar...")
    time.sleep(1.5)
    print("Debes usar todo lo que has aprendido hasta ahora.")
    time.sleep(2)

    return True  # La verificación de objetos y código se hace en la función que llama
