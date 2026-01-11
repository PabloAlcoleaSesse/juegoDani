# Sistema de Navegación Centralizado

Este documento explica cómo funciona el sistema de navegación entre habitaciones en el juego.

## ¿Por qué este sistema?

Antes teníamos un problema de **recursión infinita**: cada función de habitación llamaba directamente a la siguiente habitación, lo que creaba un stack infinito de llamadas:

```
opcionesCeldaProtagonista()
  └─> opcionesPasilloDeCeldas()
      └─> opcionesCeldaProtagonista()
          └─> opcionesPasilloDeCeldas()
              └─> ... (stack overflow!)
```

Con el nuevo sistema, tenemos un **bucle principal** que gestiona todas las transiciones:

```
flujoPrincipal() → bucle infinito
  ├─> procesarHabitacion() → ejecuta opciones de habitación actual
  ├─> retorna nueva_habitacion (o None)
  └─> cambiarHabitacion() → actualiza habitación actual
```

## Cómo funciona

### 1. Clase Partida (inicioJuego.py)

```python
class Partida:
    def __init__(self, jugador1):
        self.jugador1 = jugador1
        self.habitacionActual = hab.celdaProtagonista
        self.inventario = Inventario()
        self.juegoActivo = True  # Control del bucle principal
```

**Atributos importantes:**
- `habitacionActual`: La habitación donde está el jugador ahora
- `juegoActivo`: Controla si el juego continúa o termina
- `inventario`: El inventario del jugador

### 2. Métodos de navegación

#### `procesarHabitacion(self)`
Determina qué función de opciones ejecutar según la habitación actual:

```python
def procesarHabitacion(self):
    if self.habitacionActual == hab.celdaProtagonista:
        return opcionesCeldaProtagonista(self)
    elif self.habitacionActual == hab.pasilloDeCeldas:
        return opcionesPasilloDeCeldas(self)
    # ... más habitaciones
```

#### `cambiarHabitacion(self, nueva_habitacion)`
Actualiza la habitación actual y ejecuta la entrada:

```python
def cambiarHabitacion(self, nueva_habitacion):
    if nueva_habitacion:
        self.habitacionActual = nueva_habitacion
        tools.pasarFase()
        self.habitacionActual.entrar()
```

### 3. Funciones de opciones de habitaciones

Cada habitación tiene su propia función de opciones que **RETORNA** la siguiente habitación en lugar de llamarla directamente:

```python
def opcionesCeldaProtagonista(self):
    EstadoMenu = True
    
    while EstadoMenu:
        print("\nOpciones disponibles en la celda:")
        # ... mostrar opciones ...
        
        opcion = int(input("Elige una opción: "))
        
        if opcion == 8:  # Salir de la celda
            print("Sales de la celda...")
            EstadoMenu = False
            return hab.pasilloDeCeldas  # RETORNA, no llama
    
    return None  # Si no cambia de habitación
```

### 4. Bucle principal (flujoPrincipal)

El bucle principal coordina todo:

```python
def flujoPrincipal(self, jugador):
    # Introducción del juego
    print(f"Partida iniciada para {jugador.nombre}")
    Bienvenida(jugador.nombre)
    self.habitacionActual.entrar()
    
    # BUCLE PRINCIPAL - evita recursión
    while self.juegoActivo:
        nueva_habitacion = self.procesarHabitacion()
        
        if nueva_habitacion:
            self.cambiarHabitacion(nueva_habitacion)
        # Si no hay nueva habitación, continúa en la actual
```

## Flujo de ejemplo

Veamos qué pasa cuando el jugador va de la celda al pasillo y vuelve:

```
1. Jugador está en: Celda del Protagonista
   └─> flujoPrincipal ejecuta procesarHabitacion()
       └─> procesarHabitacion() llama a opcionesCeldaProtagonista(self)
           └─> Jugador elige opción 8 (salir)
           └─> opcionesCeldaProtagonista retorna hab.pasilloDeCeldas
   
2. nueva_habitacion = hab.pasilloDeCeldas
   └─> flujoPrincipal ejecuta cambiarHabitacion(hab.pasilloDeCeldas)
       └─> self.habitacionActual = hab.pasilloDeCeldas
       └─> hab.pasilloDeCeldas.entrar()
   
3. Jugador está en: Pasillo de Celdas
   └─> flujoPrincipal ejecuta procesarHabitacion()
       └─> procesarHabitacion() llama a opcionesPasilloDeCeldas(self)
           └─> Jugador elige opción 7 (volver a celda)
           └─> opcionesPasilloDeCeldas retorna hab.celdaProtagonista
   
4. nueva_habitacion = hab.celdaProtagonista
   └─> flujoPrincipal ejecuta cambiarHabitacion(hab.celdaProtagonista)
       └─> self.habitacionActual = hab.celdaProtagonista
       └─> hab.celdaProtagonista.entrar()
   
5. ¡De vuelta en la celda! Y sin recursión infinita.
```

## Cómo agregar una nueva habitación

### Paso 1: Definir la habitación en habitaciones.py
```python
nuevaHabitacion = habitacion("Nombre", "Descripción de la habitación")
```

### Paso 2: Crear función de opciones en inicioJuego.py
```python
def opcionesNuevaHabitacion(self):
    """Opciones de la nueva habitación. Retorna siguiente habitación o None."""
    EstadoMenu = True
    
    while EstadoMenu:
        print("\nOpciones disponibles:")
        print("1. Hacer algo")
        print("2. Volver al pasillo")
        
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            print("Haces algo...")
        elif opcion == 2:
            print("Vuelves al pasillo")
            EstadoMenu = False
            return hab.pasilloDeCeldas  # RETORNA la habitación destino
    
    return None  # Si no cambia de habitación
```

### Paso 3: Registrar en procesarHabitacion()
```python
def procesarHabitacion(self):
    if self.habitacionActual == hab.celdaProtagonista:
        return opcionesCeldaProtagonista(self)
    # ... otras habitaciones ...
    elif self.habitacionActual == hab.nuevaHabitacion:
        return opcionesNuevaHabitacion(self)  # AGREGAR AQUÍ
    return None
```

### Paso 4: Agregar acceso desde otra habitación
```python
def opcionesPasilloDeCeldas(self):
    # ...
    elif opcion == 9:  # Nueva opción
        print("Accedes a la nueva habitación")
        EstadoMenu = False
        return hab.nuevaHabitacion  # RETORNA la nueva habitación
```

## Ventajas del sistema

✅ **Sin recursión infinita**: El bucle principal gestiona todo
✅ **Fácil de depurar**: El flujo es lineal y claro
✅ **Flexible**: Puedes ir a cualquier habitación desde cualquier otra
✅ **Escalable**: Agregar nuevas habitaciones es simple
✅ **Control centralizado**: Un solo punto controla toda la navegación

## Reglas importantes

1. ⚠️ **NUNCA** llames directamente a otra función de opciones desde dentro de una función de opciones
2. ✅ **SIEMPRE** retorna la habitación destino
3. ✅ Si el jugador no cambia de habitación (ej: ver inventario), retorna `None`
4. ✅ Usa `EstadoMenu = False` antes de retornar una nueva habitación
5. ✅ Registra todas las habitaciones en `procesarHabitacion()`

## Inventario

El inventario ahora usa objetos de la clase `Objeto` definida en `objetos.py`:

```python
# Añadir objeto al inventario
self.inventario.añadirObjeto(obj.llaveOxidada)

# Verificar si tiene un objeto
if self.inventario.tieneObjeto(obj.llaveOxidada):
    print("Tienes la llave!")

# Mostrar inventario
self.inventario.mostrarInventario()

# Eliminar objeto
self.inventario.eliminarObjeto(obj.gachas)
```

## Variables globales

Algunas variables de estado del juego son globales:

```python
PuertaCeldaAbierta = False  # Estado de la puerta de la celda
```

Para modificarlas dentro de una función, usa `global`:

```python
def opcionesCeldaProtagonista(self):
    global PuertaCeldaAbierta  # Declarar como global
    
    if opcion == 5:
        PuertaCeldaAbierta = True  # Ahora sí se modifica
```

## Terminar el juego

Para terminar el juego, simplemente cambia `self.juegoActivo` a `False`:

```python
def opcionesSalidaFinal(self):
    if opcion == 1:  # Escapar
        print("¡HAS ESCAPADO! ¡Felicidades!")
        self.juegoActivo = False  # Termina el bucle principal
        return None
```

---

**Autor**: Sistema de navegación centralizado v1.0
**Fecha**: 2024
**Proyecto**: Juego de Escape de Prisión