class habitacion:
    def __init__(self, nombre, descripcion, objetos=None):
        self. nombre = nombre
        self.descripcion = descripcion
        self.objetos = objetos 
        self.isVisitada = False
    
    
    def entrar(self):
        print (f"Has entrado en la habitacion: {self.nombre}"
               f"\n{self.descripcion}"
        )
        self.isVisitada = True
        
    

celdaProtagonista = habitacion("Celda del Protagonista", "Una celda oscura y fria con barrotes oxidados. Hay un catre en una esquina y un pequeño retrete en la otra.", ["cama rota", "retrete sucio"])