class Inventario: 
    def __init__(self):
        self.items = []
    
    def agregar_item(self, item):
        self.items.append(item)
    
    def mostrar_inventario(self):
        return self.items
    
    