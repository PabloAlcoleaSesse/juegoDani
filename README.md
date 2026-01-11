# 🔓 ESCAPE DE LA PRISIÓN

Un juego de aventura de texto estilo "escape room" desarrollado en Python.

## 📖 Descripción

Has sido encarcelado injustamente y despiertas en una celda oscura sin recordar cómo llegaste allí. Tu único objetivo es **escapar** resolviendo acertijos, puzzles y descubriendo los secretos oscuros de esta prisión antigua.

Mientras avanzas, descubrirás:
- 🔍 Túneles ocultos
- 📝 Mensajes de antiguos prisioneros
- 🧪 Evidencia de experimentos secretos
- 🎭 La verdad sobre por qué estás aquí

## 🎮 Características

- **8 habitaciones únicas** para explorar
- **6 puzzles desafiantes** que requieren lógica y observación
- **13+ objetos** para recolectar y usar
- **Sistema de inventario interactivo** con descripciones detalladas
- **Narrativa inmersiva** con toques de humor negro
- **Easter eggs y secretos** para descubrir
- **Final misterioso** que te dejará pensando...

## 🚀 Cómo Jugar

### Requisitos
- Python 3.6 o superior
- No se requieren librerías externas

### Instalación y Ejecución

```bash
# Navega al directorio del juego
cd juegoDani

# Ejecuta el juego
python main.py
```

### Controles

El juego se controla completamente mediante números:
1. Lee las opciones disponibles en cada habitación
2. Escribe el número de la opción que deseas ejecutar
3. Presiona ENTER para confirmar
4. Usa la opción "Ver inventario" para revisar tus objetos

## 🗺️ Recorrido del Juego

```
Celda → Pasillo → Comedor → Almacén → Sala de Control → 
Patio → Túneles → Salida Final → ¡LIBERTAD!
```

## 📚 Documentación

- **[GUIA_COMPLETA.md](GUIA_COMPLETA.md)** - Guía completa con soluciones de todos los puzzles
- **[CAMBIOS_IMPLEMENTADOS.md](CAMBIOS_IMPLEMENTADOS.md)** - Resumen técnico de implementación

## 🎯 Objetivos del Juego

1. ✅ Escapa de tu celda inicial
2. ✅ Consigue acceso a diferentes áreas de la prisión
3. ✅ Resuelve puzzles para obtener objetos clave
4. ✅ Descubre la verdad sobre la prisión
5. ✅ Encuentra la salida secreta
6. ✅ Abre la puerta final usando todo lo aprendido
7. ✅ ¡ESCAPA!

## 🧩 Puzzles Incluidos

- 🔢 **Candado Numérico** - Descifra el código oculto
- 🔘 **Secuencia de Interruptores** - Encuentra el orden correcto
- ⚡ **Panel Eléctrico** - Repara el sistema de seguridad
- 📹 **Cámaras de Seguridad** - Desactiva en la secuencia correcta
- 🧭 **Navegación en Túneles** - Encuentra el camino correcto
- 🚪 **Puzzle Final** - Combina todo lo aprendido

## 💡 Consejos

- 📝 Lee todas las notas y documentos cuidadosamente
- 🔍 Examina todo lo que puedas antes de avanzar
- 🎒 Revisa tu inventario regularmente
- 🤔 Las pistas están dispersas por todo el juego
- ⚠️ **NO interrogues al policía** en la sala de control

## 🎭 Características Especiales

### Sistema de Inventario
- Menú interactivo con navegación numérica
- Descripciones detalladas de cada objeto
- Visualización organizada de todos tus items

### Narrativa Dinámica
- Diálogos con personalidad del protagonista
- Pausas narrativas para mejor inmersión
- Mensajes atmosféricos y descriptivos

### Easter Eggs
- 🗿 Cita filosófica de Schopenhauer
- 💪 Gimnasio exterior (sin beneficio real)
- 🥤 Referencias humorísticas
- 💀 Múltiples finales alternativos (game over)

## 📦 Estructura del Proyecto

```
juegoDani/
├── main.py                    # Punto de entrada
├── inicioJuego.py            # Lógica principal y habitaciones
├── habitaciones.py           # Definición de habitaciones
├── objetos.py               # Definición de objetos
├── puzles.py                # Implementación de puzzles
├── inventario.py            # Sistema de inventario
├── jugador.py               # Clase del jugador
├── menu.py                  # Menú principal
├── parser.py                # Utilidades de guardado
├── herramientas.py          # Funciones auxiliares
├── README.md                # Este archivo
├── GUIA_COMPLETA.md         # Guía con soluciones
└── CAMBIOS_IMPLEMENTADOS.md # Documentación técnica
```

## 🎲 Habitaciones

1. **Celda del Protagonista** - Tu punto de partida
2. **Pasillo de Celdas** - Hub central de navegación
3. **Comedor de Presos** - Área social con objetos clave
4. **Almacén** - Repleto de cajas y mecanismos misteriosos
5. **Sala de Control** - Centro de seguridad de la prisión
6. **Patio Exterior** - Primera vista del cielo nocturno
7. **Túneles Subterráneos** - Laberinto oscuro y húmedo
8. **Salida Final** - Tu última prueba antes de la libertad

## 📊 Estadísticas

- **Tiempo de juego:** 30-45 minutos (primera vez)
- **Objetos totales:** 13 coleccionables
- **Puzzles:** 6 principales + acertijos secundarios
- **Habitaciones:** 8 únicas
- **Líneas de código:** 900+ líneas
- **Finales posibles:** 2 (escape exitoso + game over)

## ⚠️ Advertencias

### ¡NO HAGAS ESTO!
- ❌ Interrogar al policía en la sala de control (pierdes el juego)
- ❌ Avanzar a los túneles sin linterna
- ❌ Intentar navegar sin el mapa

### Errores Comunes
- Olvidar recoger objetos antes de cambiar de habitación
- No leer las notas cuidadosamente
- Intentar puzzles sin las pistas necesarias

## 🏆 ¿Atascado?

Si necesitas ayuda:
1. Revisa tu inventario y lee las descripciones
2. Examina todas las opciones disponibles en tu ubicación actual
3. Revisa las notas y documentos que hayas encontrado
4. Consulta **GUIA_COMPLETA.md** para soluciones detalladas

## 🔐 Códigos Rápidos (SPOILERS)

<details>
<summary>⚠️ Clic aquí solo si estás realmente atascado</summary>

- **Candado del pasillo:** `8755`
- **Interruptores del almacén:** `3, 1, 5`
- **Cámaras de seguridad:** `1, 2, 4, 3`
- **Túneles:** `1 (izq), 2 (recto), 3 (der)`
- **Código final:** `314`

</details>

## 🎨 Tono y Ambientación

- 🌙 **Atmósfera:** Oscura, tensa y misteriosa
- 😏 **Humor:** Toques irónicos y comentarios sarcásticos
- 🎭 **Narrativa:** Historia profunda con final abierto
- 🧩 **Gameplay:** Lógica y observación

## 🛠️ Desarrollo

### Características Técnicas
- Programación orientada a objetos en Python
- Sistema modular con separación de responsabilidades
- Manejo de estados global y local
- Sistema de navegación basado en retornos
- Gestión de inventario con clases

### Futuras Mejoras Posibles
- [ ] Sistema de guardado/carga (estructura ya preparada)
- [ ] Múltiples finales según decisiones
- [ ] Más puzzles opcionales
- [ ] Sistema de pistas integrado
- [ ] Modo historia extendida

## 👥 Créditos

**Desarrollado para:** Dani  
**Género:** Aventura de Texto / Escape Room  
**Motor:** Python 3  
**Modo:** Un jugador  
**Estado:** Completo ✅

## 📜 Licencia

Este proyecto es un desarrollo personal para fines educativos y de entretenimiento.

## 🆘 Soporte

Si encuentras algún bug o tienes sugerencias:
1. Revisa la documentación en GUIA_COMPLETA.md
2. Verifica que tienes Python 3.6+
3. Asegúrate de ejecutar desde el directorio correcto

---

## 🎮 ¡Disfruta el Juego!

```
╔════════════════════════════════════════╗
║   ESCAPE DE LA PRISIÓN                ║
║   ¿Podrás encontrar la salida?        ║
║   ¿O descubrirás la verdad primero?   ║
╚════════════════════════════════════════╝
```

**¡Buena suerte escapando!** 🔓🏃‍♂️

---

*"No todos los que escaparon lo hicieron libres..."*