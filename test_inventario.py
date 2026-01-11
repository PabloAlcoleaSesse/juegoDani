#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script de prueba para el nuevo menú interactivo del inventario
"""

from inventario import Inventario
import objetos as obj

def test_menu_inventario():
    """Prueba el menú interactivo del inventario"""
    print("=" * 60)
    print("PRUEBA DEL MENÚ INTERACTIVO DEL INVENTARIO")
    print("=" * 60)

    # Crear inventario de prueba
    inventario = Inventario()

    # Agregar algunos objetos
    print("\n✓ Agregando objetos al inventario...\n")
    inventario.añadirObjeto(obj.llaveOxidada)
    inventario.añadirObjeto(obj.nota)
    inventario.añadirObjeto(obj.linterna)
    inventario.añadirObjeto(obj.destornillador)
    inventario.añadirObjeto(obj.tarjetaMagnetica)

    print("\n" + "=" * 60)
    print("INSTRUCCIONES:")
    print("=" * 60)
    print("1. Verás una lista numerada de todos los items")
    print("2. Escribe el número del item que quieres ver en detalle")
    print("3. Se mostrará el nombre y descripción completa del item")
    print("4. Presiona ENTER para volver a la lista")
    print("5. Escribe 0 para salir del inventario")
    print("=" * 60)

    input("\nPresiona ENTER para abrir el menú del inventario...")

    # Mostrar el menú interactivo
    inventario.menu_inventario()

    print("\n✓ Prueba completada. ¡El menú funciona correctamente!")

def test_inventario_vacio():
    """Prueba el menú con inventario vacío"""
    print("\n" + "=" * 60)
    print("PRUEBA CON INVENTARIO VACÍO")
    print("=" * 60)

    inventario = Inventario()
    inventario.menu_inventario()

    print("✓ Prueba de inventario vacío completada.")

if __name__ == "__main__":
    try:
        # Ejecutar prueba principal
        test_menu_inventario()

        # Preguntar si quiere probar inventario vacío
        print("\n" + "=" * 60)
        opcion = input("\n¿Quieres probar el inventario vacío? (s/n): ").lower()
        if opcion == 's':
            test_inventario_vacio()

        print("\n¡Todas las pruebas completadas!")

    except KeyboardInterrupt:
        print("\n\n✓ Prueba interrumpida por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error durante la prueba: {e}")
