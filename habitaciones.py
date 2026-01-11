class habitacion:
    def __init__(self, nombre, descripcion, objetos=None):
        self. nombre = nombre
        self.descripcion = descripcion
        self.isVisitada = False
    
    
    def entrar(self):
        print (f"Has entrado en la habitacion: {self.nombre}"
               f"\n{self.descripcion}"
        )
        self.isVisitada = True
        
    

celdaProtagonista = habitacion("Celda del Protagonista", "Una celda oscura y fria con barrotes oxidados. Hay un catre en una esquina y un pequeño retrete en la otra.")
pasilloDeCeldas = habitacion("Pasillo de Celdas", "Zona alargada con varias puertas cerradas, tuberías, cámaras y una caja metálica.")
almacen = habitacion("Almacén", "Repleto de cajas llenas de polvo y mecanismos raros.")
salaControl = habitacion("Sala de Control", "Resolver el puzzle de interruptores que abre un compartimento secreto.")
patioExterior = habitacion("Patio Exterior", "El jugador ve el cielo nocturno por primera vez. Hay una trampilla metálica hacia abajo cerrada con una cerradura digital.")
tunelesSubterraneos = habitacion("Túneles Subterráneos", "Oscuros, húmedos, laberínticos. Aquí se usa la linterna y el mapa roto.")
comedorPresos= habitacion("Comedor de Presos","Grandes mesas, olores sospechosos, un policía dormido con un pañuelo a su lado y carteles absurdos.")
salidaFinal = habitacion("Salida Final", "Una puerta blindada con un panel de control que requiere una tarjeta de seguridad avanzada para abrirse.")


