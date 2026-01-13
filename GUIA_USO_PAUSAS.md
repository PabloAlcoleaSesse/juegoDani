# GUÍA RÁPIDA: USO DE PAUSAS Y TRANSICIONES

## 📖 Introducción

Este documento es una guía rápida para entender y usar correctamente las mejoras de experiencia del usuario implementadas en el juego.

---

## 🎯 Dos Herramientas Principales

### 1. `time.sleep(segundos)`
**Pausas automáticas** - El juego espera un tiempo determinado

```python
import time

print("Has encontrado una llave misteriosa...")
time.sleep(2)  # Espera 2 segundos
print("¿Qué abrirá?")
```

### 2. `tools.pasarFase()`
**Pausas interactivas** - El jugador presiona Enter para continuar

```python
import herramientas as tools

print("Has completado el puzzle.")
tools.pasarFase()  # Muestra "Presiona Enter..." y limpia pantalla
```

---

## ⏱️ Tabla de Tiempos Recomendados

| Duración | Uso | Ejemplo |
|----------|-----|---------|
| **0.5 seg** | Efectos cortos, feedback inmediato | `*CLIC*`, `*BEEP*` |
| **1 seg** | Mensajes simples | "Examinas la puerta..." |
| **1.5 seg** | Acciones normales | "Encuentras un objeto." |
| **2 seg** | Narrativa importante | Descubrimientos, diálogos |
| **2-3 seg** | Momentos dramáticos | Revelaciones, finales |

---

## 📝 Ejemplos Prácticos

### Ejemplo 1: Acción Simple
```python
tools.clear()
print("Revisas la caja metálica.")
time.sleep(1.5)
print("Está cerrada con candado.")
time.sleep(1)
tools.pasarFase()
```

### Ejemplo 2: Encontrar un Objeto
```python
tools.clear()
print("Buscas entre los escombros...")
time.sleep(2)
print("¡Has encontrado una llave!")
time.sleep(1)
inventario.añadirObjeto(llave)
print("Llave añadida al inventario.")
time.sleep(1.5)
tools.pasarFase()
```

### Ejemplo 3: Secuencia Dramática
```python
tools.clear()
print("Te acercas a la puerta de salida...")
time.sleep(2)
print("Insertas la última llave...")
time.sleep(2)
print("*CLIC*")
time.sleep(1)
print("¡LA PUERTA SE ABRE!")
time.sleep(2.5)
print("¡HAS ESCAPADO!")
time.sleep(3)
tools.pasarFase()
```

### Ejemplo 4: Efecto de Sonido
```python
print("Golpeas la máquina expendedora...")
time.sleep(1)
print("¡PUM!")
time.sleep(0.5)
print("Cae una moneda al suelo.")
time.sleep(1.5)
```

---

## 🎨 Efectos de Sonido Textuales

Añade vida al juego con efectos de sonido escritos:

| Efecto | Uso | Pausa Recomendada |
|--------|-----|-------------------|
| `*CLIC*` | Cerraduras, botones | 0.5-1 seg |
| `*BEEP*` | Electrónica | 0.5 seg |
| `*BZZZZT*` | Error, electricidad | 1 seg |
| `*CHISPAS*` | Cables, panel | 1 seg |
| `¡CLIC! ¡CLIC!` | Múltiples seguros | 1 seg |
| `PUM!` | Golpes | 0.5-1 seg |
| `*WEEEE-OOOO*` | Alarmas | 1.5 seg |

---

## 🎭 Formato Visual

### Banner de Sección
```python
print("\n" + "=" * 60)
print("           TÍTULO DE LA SECCIÓN")
print("=" * 60)
time.sleep(1)
```

### Lista con Pausas
```python
print("Ves tres objetos:")
time.sleep(1)
print("1. Una llave oxidada")
time.sleep(0.5)
print("2. Un destornillador")
time.sleep(0.5)
print("3. Una nota arrugada")
time.sleep(1)
```

---

## 🔄 Flujo Típico de una Acción

```python
# 1. Limpiar pantalla
tools.clear()

# 2. Mostrar acción
print("Intentas abrir la puerta...")
time.sleep(1.5)

# 3. Verificar condición
if tienes_llave:
    # 4. Éxito con efectos
    print("Usas la llave.")
    time.sleep(1)
    print("*CLIC*")
    time.sleep(0.5)
    print("¡La puerta se abre!")
    time.sleep(2)
else:
    # 4. Fallo con mensaje
    print("La puerta está cerrada.")
    time.sleep(1.5)
    print("Necesitas una llave.")
    time.sleep(1)

# 5. Pausa interactiva
tools.pasarFase()
```

---

## ✅ Reglas de Oro

1. **Siempre limpia la pantalla** antes de mostrar información importante
   ```python
   tools.clear()
   ```

2. **Usa `time.sleep()` para lectura**, no solo decoración
   - Da tiempo real para leer el texto

3. **Usa `tools.pasarFase()` para control del jugador**
   - Después de eventos importantes
   - Antes de cambiar de escena
   - Al completar acciones significativas

4. **Más corto para efectos, más largo para narrativa**
   - Efectos: 0.5-1 seg
   - Narrativa: 1.5-2 seg
   - Drama: 2-3 seg

5. **No abuses de las pausas largas**
   - El jugador debe sentir fluidez, no lentitud

---

## ❌ Errores Comunes a Evitar

### ❌ MAL: Sin pausas
```python
print("Has encontrado algo.")
print("Es una llave.")
print("La guardas.")
```

### ✅ BIEN: Con pausas apropiadas
```python
print("Has encontrado algo...")
time.sleep(1.5)
print("¡Es una llave!")
time.sleep(1)
print("La guardas en tu inventario.")
time.sleep(1.5)
```

---

### ❌ MAL: Pausas muy largas
```python
print("Miras alrededor.")
time.sleep(5)  # Demasiado largo
print("No ves nada.")
```

### ✅ BIEN: Pausas equilibradas
```python
print("Miras alrededor con atención...")
time.sleep(1.5)
print("No ves nada fuera de lo común.")
time.sleep(1)
```

---

### ❌ MAL: No usar tools.pasarFase()
```python
print("Has completado el puzzle.")
# El menú aparece inmediatamente
mostrar_menu()
```

### ✅ BIEN: Dar control al jugador
```python
print("¡Has completado el puzzle!")
time.sleep(2)
print("Un compartimento secreto se abre...")
time.sleep(1.5)
tools.pasarFase()
mostrar_menu()
```

---

## 🎮 Casos de Uso Especiales

### Cambio de Habitación
```python
def cambiarHabitacion(nueva_habitacion):
    print(f"Te diriges a {nueva_habitacion.nombre}...")
    time.sleep(1.5)
    tools.pasarFase()
    nueva_habitacion.entrar()
```

### Diálogo Importante
```python
print("Guardia: '¿Qué haces aquí?'")
time.sleep(2)
print("Tú: 'Yo... me perdí...'")
time.sleep(2)
print("Guardia: 'No te creo.'")
time.sleep(2)
tools.pasarFase()
```

### Puzzle Completado
```python
print("Insertas el último número...")
time.sleep(2)
print("*BEEP* *BEEP* *BEEP*")
time.sleep(1)
print("¡CÓDIGO CORRECTO!")
time.sleep(1.5)
print("El panel se ilumina en verde.")
time.sleep(2)
tools.pasarFase()
```

---

## 📊 Resumen Visual

```
┌─────────────────────────────────────┐
│  INICIO DE ACCIÓN                   │
├─────────────────────────────────────┤
│  tools.clear()                      │
│  ↓                                  │
│  Texto descriptivo                  │
│  ↓                                  │
│  time.sleep(1-2 seg)                │
│  ↓                                  │
│  Resultado/Efecto                   │
│  ↓                                  │
│  time.sleep(1-2 seg)                │
│  ↓                                  │
│  tools.pasarFase()                  │
│  ↓                                  │
│  SIGUIENTE ACCIÓN                   │
└─────────────────────────────────────┘
```

---

## 🚀 Inicio Rápido

Para añadir pausas a una nueva función:

1. **Importa las herramientas:**
   ```python
   import time
   import herramientas as tools
   ```

2. **Limpia la pantalla al inicio:**
   ```python
   tools.clear()
   ```

3. **Añade pausas entre mensajes:**
   ```python
   print("Mensaje 1")
   time.sleep(1.5)
   print("Mensaje 2")
   time.sleep(1)
   ```

4. **Termina con pasarFase:**
   ```python
   tools.pasarFase()
   ```

---

## 📚 Recursos

- **MEJORAS_EXPERIENCIA_USUARIO.md** - Documentación completa
- **herramientas.py** - Funciones de utilidad
- **inicioJuego.py** - Ejemplos de implementación

---

**Última actualización:** 2024  
**Versión:** 1.0  
**Desarrollado para:** Dani