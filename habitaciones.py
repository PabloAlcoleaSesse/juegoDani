class habitacion:
    def __init__(self, nombre, descripcion, objetos=None):
        self. nombre = nombre
        self.descripcion = descripcion
        self.objetos = objetos 
        self.isVisitada = False
    
    
    def entrar(self, inventario):
        print (f"Has entrado en la habitacion: {self.nombre}"
               f"\n{self.descripcion}"
        )
        self.isVisitada = True
        
    