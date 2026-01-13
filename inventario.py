import time

import herramientas as tools


class Inventario:
    def __init__(self):
        self.items = []

    def menu_inventario(self):
        """Muestra un menú interactivo del inventario donde se puede ver cada item en detalle"""
        if not self.items:
            tools.clear()
            print("\n📦 Tu inventario está vacío.")
            time.sleep(1.5)
            tools.pasarFase()
            return

        while True:
            tools.clear()
            print("\n" + "=" * 50)
            print("📦 INVENTARIO")
            print("=" * 50)
            time.sleep(0.5)

            for i, item in enumerate(self.items, 1):
                if hasattr(item, "nombre"):
                    print(f"{i}. {item.nombre}")
                else:
                    print(f"{i}. {item}")

            print(f"\n0. Salir del inventario")
            print("=" * 50)

            try:
                opcion = input(
                    "\nSelecciona un número para ver detalles (0 para salir): "
                ).strip()

                if opcion == "0":
                    print("\n✓ Cerrando inventario...")
                    time.sleep(1)
                    break

                indice = int(opcion) - 1

                if 0 <= indice < len(self.items):
                    item = self.items[indice]
                    self._mostrar_detalle_item(item)
                else:
                    print("\n❌ Número inválido. Intenta de nuevo.")
                    time.sleep(1.5)
                    tools.pasarFase()

            except ValueError:
                print("\n❌ Por favor, ingresa un número válido.")
                time.sleep(1.5)
                tools.pasarFase()
            except KeyboardInterrupt:
                print("\n\n✓ Cerrando inventario...")
                time.sleep(1)
                break

    def _mostrar_detalle_item(self, item):
        """Muestra los detalles de un item específico"""
        tools.clear()
        print("\n" + "=" * 50)
        print("🔍 DETALLE DEL ITEM")
        print("=" * 50)
        time.sleep(0.5)

        if hasattr(item, "nombre"):
            print(f"\n📌 Nombre: {item.nombre}")
        else:
            print(f"\n📌 Nombre: {item}")

        if hasattr(item, "descripcion"):
            print(f"\n📝 Descripción:\n{item.descripcion}")
        else:
            print("\n📝 Descripción: No disponible")

        print("\n" + "=" * 50)
        time.sleep(1)
        tools.pasarFase()

    def añadirObjeto(self, item):
        """Añade un objeto al inventario"""
        if item not in self.items:
            self.items.append(item)
            if hasattr(item, "nombre"):
                print(f"✓ {item.nombre} añadido al inventario.")
            else:
                print(f"✓ {item} añadido al inventario.")
            time.sleep(0.5)
        else:
            print("Ya tienes este objeto en tu inventario.")
            time.sleep(1)

    def agregar_item(self, item):
        """Alias para añadirObjeto (compatibilidad)"""
        self.añadirObjeto(item)

    def eliminarObjeto(self, item):
        """Elimina un objeto del inventario"""
        if item in self.items:
            self.items.remove(item)
            if hasattr(item, "nombre"):
                print(f"✗ {item.nombre} eliminado del inventario.")
            else:
                print(f"✗ {item} eliminado del inventario.")
            time.sleep(1)
            return True
        else:
            print("No tienes este objeto en tu inventario.")
            time.sleep(1)
            return False

    def eliminar_item(self, item):
        """Alias para eliminarObjeto (compatibilidad)"""
        return self.eliminarObjeto(item)

    def tieneObjeto(self, item):
        """Verifica si el jugador tiene un objeto específico"""
        return item in self.items

    def tiene_item(self, item):
        """Alias para tieneObjeto (compatibilidad)"""
        return self.tieneObjeto(item)

    def buscarPorNombre(self, nombre):
        """Busca un objeto por su nombre"""
        for item in self.items:
            if hasattr(item, "nombre") and item.nombre.lower() == nombre.lower():
                return item
        return None

    def mostrarInventario(self):
        """Muestra todos los objetos del inventario con sus descripciones"""
        if not self.items:
            print("\n📦 Tu inventario está vacío.")
            time.sleep(1)
            return

        print("\n" + "=" * 50)
        print("📦 INVENTARIO")
        print("=" * 50)
        time.sleep(0.5)
        for i, item in enumerate(self.items, 1):
            if hasattr(item, "nombre") and hasattr(item, "descripcion"):
                print(f"{i}. {item.nombre}")
                print(f"   └─ {item.descripcion}")
            else:
                print(f"{i}. {item}")
        print("=" * 50 + "\n")
        time.sleep(1)

    def mostrar_inventario(self):
        """Alias para mostrarInventario (compatibilidad)"""
        self.mostrarInventario()

    def estaVacio(self):
        """Verifica si el inventario está vacío"""
        return len(self.items) == 0

    def cantidadItems(self):
        """Retorna la cantidad de items en el inventario"""
        return len(self.items)

    def listarNombres(self):
        """Retorna una lista con los nombres de todos los objetos"""
        nombres = []
        for item in self.items:
            if hasattr(item, "nombre"):
                nombres.append(item.nombre)
            else:
                nombres.append(str(item))
        return nombres
