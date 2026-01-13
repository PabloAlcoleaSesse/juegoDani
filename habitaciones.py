import time

import herramientas as tools


class habitacion:
    def __init__(self, nombre, descripcion, objetos=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.isVisitada = False

    def entrar(self):
        tools.clear()
        print("\n" + "=" * 60)
        print(f"       {self.nombre.upper()}")
        print("=" * 60)
        time.sleep(1)
        print(f"\n{self.descripcion}")
        time.sleep(2)
        self.isVisitada = True
        tools.pasarFase()


celdaProtagonista = habitacion(
    "Celda del Protagonista",
    "Una celda oscura y fría con barrotes oxidados.\nHay un catre en una esquina y un pequeño retrete en la otra.\nEl aire es pesado y huele a humedad.",
)
pasilloDeCeldas = habitacion(
    "Pasillo de Celdas",
    "Zona alargada con varias puertas cerradas.\nTuberías recorren el techo, cámaras de seguridad vigilan cada rincón.\nHay una caja metálica al final del pasillo.",
)
almacen = habitacion(
    "Almacén",
    "Repleto de cajas llenas de polvo y telarañas.\nMecanismos raros cubren las paredes.\nEl olor a moho es casi insoportable.",
)
salaControl = habitacion(
    "Sala de Control",
    "Monitores parpadean mostrando diferentes áreas de la prisión.\nUn panel eléctrico chisporrotea en la esquina.\nPapeles y documentos están esparcidos por todas partes.",
)
patioExterior = habitacion(
    "Patio Exterior",
    "El cielo nocturno se extiende sobre ti, lleno de estrellas.\nUna brisa fresca acaricia tu rostro después de tanto encierro.\nEn el suelo hay una trampilla metálica cerrada con cerradura digital.",
)
tunelesSubterraneos = habitacion(
    "Túneles Subterráneos",
    "Oscuridad total. El eco de gotas de agua resuena en las paredes.\nEl aire es húmedo y frío.\nSin luz, sería imposible encontrar la salida.",
)
comedorPresos = habitacion(
    "Comedor de Presos",
    "Grandes mesas metálicas con restos de comida.\nOlores sospechosos llenan el aire.\nUn policía duerme profundamente en una silla, con un pañuelo caído a su lado.\nCarteles absurdos cubren las paredes.",
)
salidaFinal = habitacion(
    "Salida Final",
    "Una puerta blindada imponente se alza frente a ti.\nTres mecanismos de seguridad protegen tu libertad.\nEste es el momento de la verdad.",
)
