import time
import herramientas as tools

def puzleCandado():
    """Puzzle del candado numérico en la caja metálica del pasillo"""
    estadoPuzle = True
    while estadoPuzle:
        tools.clear()
        print(
            "Para abrir el candado numérico, debes ingresar el código correcto de 4 dígitos."
        )
        print("Pista: Recuerda la nota que encontraste... (S,R,T,O)")
        print("Resolver candado: 1")
        print("Salir: 2")
        try:
            eleccion = input("Elige una opción (1-2): ")
            if eleccion != "1" and eleccion != "2":
                raise ValueError("Número fuera de rango")
            if eleccion == "2":
                estadoPuzle = False
                print("Decides no intentar abrir el candado por ahora.")
                time.sleep(1)
                return False
            codigoIngresado = input("Ingresa el código de 4 dígitos: ")
            # S=8, R=7, T=5, O=5 basado en las letras mayúsculas de la nota
            if codigoIngresado == "8755":
                tools.clear()
                print("Has ingresado el código correcto. El candado se abre.")
                time.sleep(2)
                estadoPuzle = False
                return True
            else:
                print("Código incorrecto. El candado sigue cerrado.")
                time.sleep(1)
                print("¿Hay alguna pista que hayas pasado por alto?")
                time.sleep(2)

        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, elige un número entre 1 y 2.")
            continue


def puzleInterruptores():
    """Puzzle de secuencia de interruptores en el almacén"""
    tools.clear()
    print("\n=== PANEL DE INTERRUPTORES ===")
    print("Ves un panel con 5 interruptores numerados del 1 al 5.")
    print("Parece que deben activarse en un orden específico...")
    time.sleep(2)
    print("\nRecuerdas la nota del comedor: 'El orden no es numérico, es el del castigo.'")
    print("En la pared ves marcas extrañas: III - I - V")
    time.sleep(2)

    estadoPuzle = True
    intentos = 0
    max_intentos = 3

    while estadoPuzle and intentos < max_intentos:
        print(f"\n[Intento {intentos + 1}/{max_intentos}]")
        print("Debes activar 3 interruptores en el orden correcto.")
        print("Interruptores disponibles: 1, 2, 3, 4, 5")
        print("\n¿Intentar resolver el puzzle? (s/n): ", end="")

        respuesta = input().lower()
        if respuesta != 's':
            print("Decides dejarlo para después.")
            time.sleep(1)
            return False

        secuencia = []
        for i in range(3):
            try:
                interruptor = input(f"Interruptor {i+1}: ")
                secuencia.append(interruptor)
            except:
                print("Entrada inválida.")
                intentos += 1
                continue

        # Solución: 3, 1, 5 (basado en las marcas III=3, I=1, V=5)
        if secuencia == ["3", "1", "5"]:
            tools.clear()
            print("\n¡CLIC! ¡CLIC! ¡CLIC!")
            time.sleep(1)
            print("Los interruptores se iluminan en verde.")
            print("Escuchas un sonido mecánico detrás de las cajas...")
            time.sleep(2)
            print("\n¡Un compartimento secreto se ha abierto!")
            time.sleep(2)
            return True
        else:
            intentos += 1
            print("\nNada sucede. Esa no es la secuencia correcta.")
            time.sleep(1)
            if intentos < max_intentos:
                print("Las marcas en la pared deben significar algo...")
                time.sleep(2)

    print("\nDemasiados intentos fallidos. El panel se bloquea temporalmente.")
    time.sleep(2)
    return False


def puzlePanel():
    """Puzzle para reparar el panel eléctrico en la sala de control"""
    tools.clear()
    print("\n=== PANEL ELÉCTRICO ===")
    print("El panel está dañado. Los cables cuelgan y chisporrotean.")
    print("Necesitas repararlo para restaurar el sistema.")
    time.sleep(2)

    print("\nParece que necesitas:")
    print("- Un cable para reconectar los circuitos")
    print("- Un destornillador para asegurar las conexiones")
    print("- Una tarjeta magnética para activar el sistema")
    time.sleep(2)

    return True  # Se verifica en la función que llama si tiene los objetos


def puzleCamaras():
    """Puzzle de desactivar las cámaras en el orden correcto"""
    tools.clear()
    print("\n=== SISTEMA DE SEGURIDAD ===")
    print("Ves 4 monitores mostrando diferentes áreas de la prisión:")
    print("1. Celda")
    print("2. Pasillo")
    print("3. Comedor")
    print("4. Patio")
    time.sleep(2)

    print("\nRecuerdas el documento que encontraste:")
    print("'Las cámaras miran en el mismo orden en el que caen los presos.'")
    print("\nDebes desactivar las cámaras en el orden correcto.")
    time.sleep(2)

    estadoPuzle = True
    intentos = 0
    max_intentos = 2

    while estadoPuzle and intentos < max_intentos:
        print(f"\n[Intento {intentos + 1}/{max_intentos}]")
        print("Ingresa el orden para desactivar las 4 cámaras:")

        try:
            cam1 = input("Cámara 1: ")
            cam2 = input("Cámara 2: ")
            cam3 = input("Cámara 3: ")
            cam4 = input("Cámara 4: ")

            # Orden correcto: Celda(1), Pasillo(2), Patio(4), Túneles (pero no hay túneles en la lista, así que es Comedor)
            # El orden lógico de la prisión es: Celda -> Pasillo -> Patio
            # Pero según el documento original: Celda, Pasillo, Patio, Túneles
            # Como solo hay 4 opciones, el orden es: 1, 2, 4, 3
            if [cam1, cam2, cam3, cam4] == ["1", "2", "4", "3"]:
                tools.clear()
                print("\n¡SISTEMA DESACTIVADO!")
                time.sleep(1)
                print("Las luces rojas de las cámaras se apagan una por una.")
                print("¡La seguridad del patio exterior ha sido desactivada!")
                time.sleep(2)
                return True
            else:
                intentos += 1
                print("\n¡ALARMA! Las luces parpadean.")
                time.sleep(1)
                print("Esa no es la secuencia correcta.")
                time.sleep(1)
                if intentos < max_intentos:
                    print("Piensa en el recorrido natural de un prisionero...")
                    time.sleep(2)

        except:
            intentos += 1
            print("Entrada inválida.")

    print("\nEl sistema se bloquea. No puedes intentarlo de nuevo ahora.")
    time.sleep(2)
    return False


def puzleOrientacion():
    """Puzzle de navegación en los túneles subterráneos"""
    tools.clear()
    print("\n=== TÚNELES SUBTERRÁNEOS ===")
    print("Estás en un laberinto oscuro. Tu linterna ilumina el camino.")
    print("Tienes el mapa roto. Intentas descifrar las marcas...")
    time.sleep(2)

    print("\nEn el mapa ves:")
    print("- Una flecha dibujada apuntando a la izquierda")
    print("- Gotas de agua señalando hacia adelante")
    print("- Marcas en círculo con una flecha a la derecha")
    time.sleep(2)

    camino = []

    print("\n--- PRIMERA ENCRUCIJADA ---")
    print("El túnel se divide en tres direcciones.")
    print("1. Izquierda (paredes húmedas)")
    print("2. Recto (sonido de agua goteando)")
    print("3. Derecha (olor a moho)")

    eleccion1 = input("¿Qué camino tomas? (1/2/3): ")
    camino.append(eleccion1)

    if eleccion1 != "1":
        print("\nCaminas durante un rato y llegas a un callejón sin salida.")
        time.sleep(2)
        print("Debes volver al inicio.")
        time.sleep(2)
        return False

    print("\nAvanzas por el túnel de la izquierda...")
    time.sleep(2)

    print("\n--- SEGUNDA ENCRUCIJADA ---")
    print("Otra división del camino.")
    print("1. Izquierda (muy oscuro)")
    print("2. Recto (escuchas gotas de agua)")
    print("3. Derecha (corriente de aire)")

    eleccion2 = input("¿Qué camino tomas? (1/2/3): ")
    camino.append(eleccion2)

    if eleccion2 != "2":
        print("\nEl camino se vuelve más estrecho hasta que no puedes continuar.")
        time.sleep(2)
        print("Debes retroceder al inicio.")
        time.sleep(2)
        return False

    print("\nSigues recto, las gotas de agua te guían...")
    time.sleep(2)

    print("\n--- TERCERA ENCRUCIJADA ---")
    print("La última división.")
    print("1. Izquierda (completamente oscuro)")
    print("2. Recto (paredes cerradas)")
    print("3. Derecha (ves una luz tenue a lo lejos)")

    eleccion3 = input("¿Qué camino tomas? (1/2/3): ")
    camino.append(eleccion3)

    if eleccion3 != "3":
        print("\nTe encuentras con una pared de roca sólida.")
        time.sleep(2)
        print("Este no es el camino. Vuelves al inicio.")
        time.sleep(2)
        return False

    tools.clear()
    print("\n¡Lo lograste!")
    time.sleep(1)
    print("La luz se hace más brillante a medida que avanzas.")
    print("Has navegado exitosamente por los túneles.")
    time.sleep(2)
    return True


def puzleSalidaFinal():
    """Puzzle final de la salida que combina múltiples elementos"""
    tools.clear()
    print("\n" + "=" * 60)
    print("                    SALIDA FINAL")
    print("=" * 60)
    print("\nFrente a ti hay una puerta metálica antigua.")
    print("Tiene tres mecanismos de seguridad:")
    time.sleep(2)

    print("\n1. Un lector de tarjetas de seguridad")
    print("2. Un teclado numérico")
    print("3. Un panel de acceso que requiere herramientas")

    time.sleep(2)
    print("\nEsta es tu última oportunidad de escapar...")
    print("Debes usar todo lo que has aprendido hasta ahora.")
    time.sleep(2)

    return True  # La verificación de objetos y código se hace en la función que llama
