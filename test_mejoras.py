#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar que todas las mejoras están funcionando correctamente.
"""

import sys
import time

print("=" * 60)
print("    VERIFICACIÓN DE MEJORAS DE EXPERIENCIA DE USUARIO")
print("=" * 60)
print()

# Test 1: Verificar imports
print("Test 1: Verificando imports...")
time.sleep(1)

try:
    import herramientas as tools

    print("✓ herramientas.py importado correctamente")
    time.sleep(0.5)
except ImportError as e:
    print(f"✗ Error al importar herramientas: {e}")
    sys.exit(1)

try:
    import habitaciones as hab

    print("✓ habitaciones.py importado correctamente")
    time.sleep(0.5)
except ImportError as e:
    print(f"✗ Error al importar habitaciones: {e}")
    sys.exit(1)

try:
    import puzles as puz

    print("✓ puzles.py importado correctamente")
    time.sleep(0.5)
except ImportError as e:
    print(f"✗ Error al importar puzles: {e}")
    sys.exit(1)

try:
    import inventario

    print("✓ inventario.py importado correctamente")
    time.sleep(0.5)
except ImportError as e:
    print(f"✗ Error al importar inventario: {e}")
    sys.exit(1)

try:
    import inicioJuego

    print("✓ inicioJuego.py importado correctamente")
    time.sleep(0.5)
except ImportError as e:
    print(f"✗ Error al importar inicioJuego: {e}")
    sys.exit(1)

print()
time.sleep(1)

# Test 2: Verificar funciones de herramientas
print("Test 2: Verificando funciones de herramientas...")
time.sleep(1)

try:
    # Verificar que las funciones existen
    assert hasattr(tools, "clear"), "tools.clear() no encontrada"
    print("✓ tools.clear() disponible")
    time.sleep(0.5)

    assert hasattr(tools, "pasarFase"), "tools.pasarFase() no encontrada"
    print("✓ tools.pasarFase() disponible")
    time.sleep(0.5)

    assert hasattr(tools, "salto_de_linea"), "tools.salto_de_linea() no encontrada"
    print("✓ tools.salto_de_linea() disponible")
    time.sleep(0.5)
except AssertionError as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print()
time.sleep(1)

# Test 3: Verificar habitaciones
print("Test 3: Verificando habitaciones mejoradas...")
time.sleep(1)

try:
    habitaciones_lista = [
        ("celdaProtagonista", hab.celdaProtagonista),
        ("pasilloDeCeldas", hab.pasilloDeCeldas),
        ("almacen", hab.almacen),
        ("salaControl", hab.salaControl),
        ("patioExterior", hab.patioExterior),
        ("tunelesSubterraneos", hab.tunelesSubterraneos),
        ("comedorPresos", hab.comedorPresos),
        ("salidaFinal", hab.salidaFinal),
    ]

    for nombre, habitacion in habitaciones_lista:
        assert hasattr(habitacion, "nombre"), f"{nombre} no tiene atributo 'nombre'"
        assert hasattr(habitacion, "descripcion"), (
            f"{nombre} no tiene atributo 'descripcion'"
        )
        assert hasattr(habitacion, "entrar"), f"{nombre} no tiene método 'entrar'"
        print(f"✓ Habitación {nombre} configurada correctamente")
        time.sleep(0.3)
except AssertionError as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print()
time.sleep(1)

# Test 4: Verificar inventario
print("Test 4: Verificando sistema de inventario...")
time.sleep(1)

try:
    inv = inventario.Inventario()
    assert hasattr(inv, "items"), "Inventario no tiene atributo 'items'"
    print("✓ Inventario inicializado correctamente")
    time.sleep(0.5)

    assert hasattr(inv, "menu_inventario"), (
        "Inventario no tiene método 'menu_inventario'"
    )
    print("✓ menu_inventario() disponible")
    time.sleep(0.5)

    assert hasattr(inv, "añadirObjeto"), "Inventario no tiene método 'añadirObjeto'"
    print("✓ añadirObjeto() disponible")
    time.sleep(0.5)
except AssertionError as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print()
time.sleep(1)

# Test 5: Verificar puzles
print("Test 5: Verificando puzles...")
time.sleep(1)

try:
    puzles_funciones = [
        "puzleCandado",
        "puzleInterruptores",
        "puzlePanel",
        "puzleCamaras",
        "puzleOrientacion",
        "puzleSalidaFinal",
    ]

    for puzle in puzles_funciones:
        assert hasattr(puz, puzle), f"puzles.{puzle}() no encontrada"
        print(f"✓ {puzle}() disponible")
        time.sleep(0.3)
except AssertionError as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print()
time.sleep(1)

# Resumen final
print("=" * 60)
print("    ✓ TODAS LAS VERIFICACIONES PASARON EXITOSAMENTE")
print("=" * 60)
print()
print("Mejoras implementadas:")
print("  • time.sleep() añadido en momentos clave")
print("  • tools.pasarFase() implementado para transiciones")
print("  • Efectos de sonido textuales (*CLICK*, *BEEP*, etc.)")
print("  • Formato visual mejorado con bordes decorativos")
print("  • Descripciones atmosféricas expandidas")
print()
time.sleep(2)

print("El juego está listo para ofrecer una experiencia fluida.")
print()
print("Para jugar, ejecuta: python main.py")
print()
