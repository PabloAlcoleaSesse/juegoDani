# GUÍA COMPLETA DEL JUEGO - ESCAPE DE LA PRISIÓN

## 📋 ÍNDICE
1. [Introducción](#introducción)
2. [Cómo Jugar](#cómo-jugar)
3. [Solución Completa](#solución-completa)
4. [Lista de Objetos](#lista-de-objetos)
5. [Lista de Puzzles](#lista-de-puzzles)
6. [Mapa de Habitaciones](#mapa-de-habitaciones)

---

## 🎮 INTRODUCCIÓN

**Título:** Escape de la Prisión
**Género:** Aventura de texto / Escape Room
**Objetivo:** Escapar de una prisión antigua resolviendo acertijos y puzzles

### Historia
Has sido encarcelado injustamente y despiertas sin recordar cómo llegaste allí. Mientras intentas escapar, descubres secretos oscuros sobre la prisión: experimentos, túneles ocultos y mensajes de antiguos prisioneros. Cuanto más avanzas, más evidente se vuelve que tu captura no fue un error... alguien quería que terminaras allí.

---

## 🕹️ CÓMO JUGAR

### Instalación y Ejecución
```bash
cd juegoDani
python main.py
```

### Controles
- El juego se controla completamente con números
- Lee las opciones disponibles en cada habitación
- Ingresa el número de la opción que deseas ejecutar
- Usa la opción "Ver inventario" para revisar tus objetos

### Consejos Importantes
⚠️ **NO interrogues al policía en la sala de control** - ¡Te atrapará!
💡 Lee todas las notas y documentos que encuentres
🔍 Examina todo antes de avanzar
📝 Toma nota de los códigos y pistas

---

## 🗺️ SOLUCIÓN COMPLETA (PASO A PASO)

### 1️⃣ CELDA DEL PROTAGONISTA

**Objetivo:** Encontrar la llave para salir de la celda

**Pasos:**
1. **Comerse las gachas** (Opción 1)
   - Obtienes: **Llave Oxidada**
   
2. **Revisar la pequeña estantería** (Opción 4)
   - Obtienes: **Nota con pista** (código para el candado)
   - La nota dice: "—¿Tú SabeS pOR qué lOS buzOS Se TiRan hacia aTRáS al maR?"
   - Pista oculta: Las letras mayúsculas son S, R, T, O

3. **Intentar abrir la puerta** (Opción 5)
   - Usa la llave oxidada
   - ✅ Puerta abierta

4. **Salir de la celda** (Opción 8)
   - Avanzas al Pasillo de Celdas

---

### 2️⃣ PASILLO DE CELDAS

**Objetivo:** Conseguir la tarjeta magnética para acceder al comedor

**Pasos:**
1. **Examinar la caja metálica** (Opción 2)
   - Aparece el puzzle del candado numérico
   - **Código:** `8755` (de la nota: S=8, R=7, T=5, O=5)
   - Obtienes: **Tarjeta Magnética**

2. **Acceder al comedor** (Opción 4)
   - Usa la tarjeta magnética
   - ✅ Entras al Comedor

---

### 3️⃣ COMEDOR DE PRESOS

**Objetivo:** Conseguir objetos necesarios para avanzar

**Pasos:**
1. **Examinar las mesas** (Opción 1)
   - Obtienes: **Nota con Acertijo**
   - Dice: "El orden no es numérico, es el del castigo. III - I - V"

2. **Examinar el tablón de anuncios** (Opción 4)
   - Obtienes: **Destornillador**

3. **Revisar la máquina expendedora** (Opción 6)
   - Le das un puñetazo a la máquina
   - Obtienes: **Trozo de Cable**

4. **Volver al pasillo** (Opción 7)

---

### 4️⃣ ALMACÉN (desde el Pasillo)

**Objetivo:** Conseguir la tarjeta de seguridad avanzada y la linterna

**Requisito:** Tener el destornillador

**Pasos:**
1. **Acceder al almacén** (Opción 5 en el Pasillo)
   - Usa el destornillador

2. **Examinar los mecanismos raros** (Opción 2)
   - Aparece el **Puzzle de Interruptores**
   - **Solución:** 3, 1, 5 (basado en las marcas III, I, V)
   - Obtienes: **Tarjeta de Seguridad Avanzada**
   - Obtienes: **Linterna**

3. **Volver al pasillo** (Opción 3)

---

### 5️⃣ SALA DE CONTROL (desde el Pasillo)

**Objetivo:** Reparar el panel y desactivar la seguridad del patio

**Requisito:** Tener la tarjeta de seguridad avanzada

**Pasos:**
1. **Acceder a la sala de control** (Opción 6 en el Pasillo)
   - Usa la tarjeta de seguridad avanzada

2. **Leer documentos sospechosos** (Opción 2)
   - Obtienes: **Documento Secreto**
   - Contiene: "Las cámaras miran en el mismo orden en el que caen los presos"
   - También tiene el código: **314**

3. **Revisar el suelo** (Opción 3)
   - Obtienes: **Mapa Antiguo** (de los túneles)

4. **Reparar el panel eléctrico** (Opción 4)
   - Necesitas: Trozo de Cable + Destornillador + Tarjeta Magnética
   - ✅ Panel reparado

5. **Desactivar seguridad del patio** (Opción 5)
   - Aparece el **Puzzle de Cámaras**
   - **Solución:** 1, 2, 4, 3 (Celda, Pasillo, Patio, Comedor)
   - ✅ Seguridad desactivada
   - ✅ Puerta del patio desbloqueada

⚠️ **NO elijas las opciones 6 (Matar) ni 7 (Interrogar)** - La opción 7 reinicia el juego

6. **Volver al pasillo** (Opción 8)

---

### 6️⃣ PATIO EXTERIOR (desde el Comedor)

**Objetivo:** Acceder a los túneles subterráneos

**Pasos:**
1. **Ir al comedor** (Opción 4 en el Pasillo)

2. **Abrir puerta del patio exterior** (Opción 5)
   - La puerta ya está desbloqueada desde la sala de control
   - ✅ Entras al Patio

3. **Intentar abrir la trampilla metálica** (Opción 3)
   - Usa la tarjeta de seguridad avanzada
   - ✅ Trampilla abierta
   - Desciendes a los túneles

---

### 7️⃣ TÚNELES SUBTERRÁNEOS

**Objetivo:** Navegar por los túneles hasta la salida

**Requisitos:** 
- **Linterna** (para ver)
- **Mapa Antiguo** (para orientarte)

**Pasos:**
1. **Usar la linterna** (Opción 1)
   - Iluminas los túneles

2. **Analizar el mapa roto** (Opción 2)
   - Ves las pistas:
     - Flecha izquierda
     - Gotas de agua (recto)
     - Marcas en círculo (derecha)

3. **Intentar navegar por los túneles** (Opción 3)
   - Aparece el **Puzzle de Orientación**
   - **Solución:**
     - Primera encrucijada: **1** (Izquierda)
     - Segunda encrucijada: **2** (Recto)
     - Tercera encrucijada: **3** (Derecha)
   - ✅ Llegas a la Salida Final

---

### 8️⃣ SALIDA FINAL

**Objetivo:** Abrir la puerta final y escapar

**Requisitos:**
- **Tarjeta de Seguridad Avanzada**
- **Código 314** (del documento secreto)
- **Destornillador**

**Pasos:**
1. **Examinar la puerta** (Opción 1)
   - Ves los tres mecanismos de seguridad

2. **Intentar abrir la puerta** (Opción 2)
   
   **Mecanismo 1 - Lector de Tarjetas:**
   - Se usa automáticamente la tarjeta de seguridad avanzada
   - ✅ Primer mecanismo desbloqueado

   **Mecanismo 2 - Teclado Numérico:**
   - Ingresa el código: **314**
   - ✅ Segundo mecanismo desbloqueado

   **Mecanismo 3 - Panel Manual:**
   - Se usa automáticamente el destornillador
   - ✅ Tercer mecanismo desbloqueado

3. **¡VICTORIA!**
   - La puerta se abre
   - Escapas de la prisión
   - Aparece el mensaje final misterioso...
   - 🎉 **FIN DEL JUEGO**

---

## 📦 LISTA DE OBJETOS

| Objeto | Ubicación | Cómo Obtener |
|--------|-----------|--------------|
| **Llave Oxidada** | Celda | Comerse las gachas |
| **Nota** | Celda | Revisar la estantería |
| **Tarjeta Magnética** | Pasillo | Resolver candado (código 8755) |
| **Nota con Acertijo** | Comedor | Examinar las mesas |
| **Destornillador** | Comedor | Examinar tablón de anuncios |
| **Trozo de Cable** | Comedor | Golpear máquina expendedora |
| **Tarjeta Seguridad Avanzada** | Almacén | Resolver puzzle de interruptores (3,1,5) |
| **Linterna** | Almacén | Resolver puzzle de interruptores |
| **Documento Secreto** | Sala Control | Leer documentos |
| **Mapa Antiguo** | Sala Control | Revisar el suelo |
| **Polvo** | Almacén | Revisar estantes (objeto humorístico) |
| **Pañuelo** | Comedor | Coger del suelo (opcional) |

---

## 🧩 LISTA DE PUZZLES

### 1. Candado Numérico (Pasillo)
- **Pista:** Nota con las letras mayúsculas S, R, T, O
- **Solución:** `8755`
- **Recompensa:** Tarjeta Magnética

### 2. Puzzle de Interruptores (Almacén)
- **Pista:** "El orden no es numérico, es el del castigo" + marcas III, I, V
- **Solución:** `3, 1, 5`
- **Recompensa:** Tarjeta de Seguridad Avanzada + Linterna

### 3. Reparar Panel Eléctrico (Sala Control)
- **Requisitos:** Trozo de Cable + Destornillador + Tarjeta Magnética
- **Solución:** Tener los tres objetos
- **Resultado:** Panel reparado (necesario para desactivar cámaras)

### 4. Puzzle de Cámaras (Sala Control)
- **Pista:** "Las cámaras miran en el mismo orden en el que caen los presos"
- **Solución:** `1, 2, 4, 3` (Celda, Pasillo, Patio, Comedor)
- **Resultado:** Seguridad del patio desactivada

### 5. Puzzle de Orientación (Túneles)
- **Pista:** Mapa con flecha izquierda, gotas de agua, marcas en círculo
- **Solución:** 
  - 1ª encrucijada: `1` (Izquierda)
  - 2ª encrucijada: `2` (Recto)
  - 3ª encrucijada: `3` (Derecha)
- **Resultado:** Llegas a la Salida Final

### 6. Puzzle Final (Salida)
- **Requisitos:** Tarjeta Seguridad Avanzada + Código 314 + Destornillador
- **Solución:** 
  1. Insertar tarjeta
  2. Ingresar código `314`
  3. Usar destornillador
- **Resultado:** ¡ESCAPE EXITOSO!

---

## 🗺️ MAPA DE HABITACIONES

```
┌─────────────────────────────────────────────────────────┐
│                    ESCAPE DE LA PRISIÓN                 │
└─────────────────────────────────────────────────────────┘

[1] CELDA DEL PROTAGONISTA
     ↓ (Llave Oxidada)
     
[2] PASILLO DE CELDAS
     ├→ [1] Celda (volver)
     ├→ [3] Comedor (Tarjeta Magnética)
     ├→ [4] Almacén (Destornillador)
     └→ [5] Sala Control (Tarjeta Seguridad Avanzada)
     
[3] COMEDOR DE PRESOS
     ├→ [2] Pasillo
     └→ [6] Patio Exterior (después de desactivar seguridad)
     
[4] ALMACÉN
     └→ [2] Pasillo
     
[5] SALA DE CONTROL
     └→ [2] Pasillo
     
[6] PATIO EXTERIOR
     ├→ [3] Comedor
     └→ [7] Túneles (Tarjeta Seguridad Avanzada)
     
[7] TÚNELES SUBTERRÁNEOS
     ├→ [6] Patio
     └→ [8] Salida Final (resolver puzzle de orientación)
     
[8] SALIDA FINAL
     └→ ¡LIBERTAD! (resolver puzzle final)
```

---

## 🎯 SECUENCIA ÓPTIMA

1. **Celda** → Gachas + Estantería
2. **Pasillo** → Abrir caja (8755)
3. **Comedor** → Mesas + Tablón + Máquina
4. **Almacén** → Interruptores (3,1,5)
5. **Sala Control** → Documentos + Suelo + Reparar panel + Desactivar cámaras
6. **Patio** → Abrir trampilla
7. **Túneles** → Navegar (1,2,3)
8. **Salida Final** → Usar tarjeta + código 314 + destornillador

---

## ⚠️ ADVERTENCIAS

### ❌ NO HAGAS ESTO:
- **NO interrogues al policía** en la sala de control (Opción 7) → Pierdes el juego
- **NO intentes navegar los túneles sin linterna** → No podrás avanzar
- **NO intentes navegar sin el mapa** → Te perderás

### ⚡ ERRORES COMUNES:
- Olvidar recoger objetos antes de cambiar de habitación
- No leer las notas y documentos cuidadosamente
- Intentar puzzles sin tener las pistas necesarias
- No revisar el inventario regularmente

---

## 🎮 CARACTERÍSTICAS DEL JUEGO

### Sistema de Inventario
- Presiona la opción "Ver inventario" en cualquier momento
- Examina objetos para ver sus descripciones
- Los objetos se usan automáticamente cuando son necesarios

### Sistema de Puzzles
- Algunos puzzles tienen límite de intentos
- Las pistas están dispersas por todo el juego
- Todos los puzzles son resolubles con la información disponible

### Narrativa
- Diálogos humorísticos e irónicos
- Mensajes que revelan la historia de la prisión
- Final misterioso que sugiere que la historia continúa

---

## 🏆 DATOS CURIOSOS

- **Mensaje de Schopenhauer:** En el almacén hay una cita filosófica sobre la desconfianza
- **Polvo:** Puedes encontrar polvo en el almacén (objeto humorístico sin utilidad)
- **Gimnasio exterior:** Puedes hacer ejercicio en el patio (sin beneficio)
- **Refresco carbonatado:** Referencia humorística a una marca de refrescos
- **Mejillón gigante:** Si avanzas sin luz en los túneles... ¡cuidado!

---

## 📝 CRÉDITOS

**Desarrollado para:** Dani
**Género:** Aventura de Texto / Escape Room
**Motor:** Python 3
**Modo:** Un jugador

---

## 🆘 SOPORTE

Si te quedas atascado:
1. Revisa el inventario
2. Lee todas las notas y documentos
3. Consulta esta guía
4. ¡No te rindas! Todos los puzzles tienen solución

---

**¡Buena suerte escapando de la prisión!** 🔓🏃‍♂️