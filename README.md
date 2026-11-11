# Luciérnaga (Firefly) - 2D Dark Cave Exploration

![Unity](https://img.shields.io/badge/Unity-6000.6.0f1%20LTS-black?logo=unity)
![Render Pipeline](https://img.shields.io/badge/Render%20Pipeline-URP%202D-blue)
![Input System](https://img.shields.io/badge/Input%20System-New%20Input%20System-green)
![License](https://img.shields.io/badge/License-MIT%20%2F%20CC0-yellow)

**Luciérnaga** es un videojuego 2D de exploración y plataformas atmosférico desarrollado en **Unity 6 (6000.6.0f1)** utilizando el **Universal Render Pipeline (URP 2D Lights)**.

El jugador encarna a una pequeña luciérnaga atrapada en profundas cavernas en penumbra. Su propia luz bioluminiscente es su única visión y su energía vital: se desgasta continuamente con cada segundo que pasa. Para sobrevivir y hallar la salida hacia la superficie, deberá explorar las cámaras subterráneas, esquivar murciélagos patrulleros y pinchos afilados, recolectar los ancestrales cristales de luz y activar el portal de escape.

---

## 🎮 Mecánica Central: La Luz es Vida

- **Iluminación Dinámica URP 2D:** La cueva se encuentra sumergida en oscuridad casi total (luz global al 8%). El jugador emite una luz puntual en tiempo real (`Light2D`) que ilumina su entorno inmediato.
- **Drenaje y Radio Dinámico:** A medida que la energía de la luciérnaga se agota (pérdida constante por segundo), el radio de iluminación se contrae gradualmente de un radio seguro de 6.5 metros hasta un rango crítico de 1.2 metros.
- **Tensión Crítica:** Al caer por debajo del 25% de energía, la luz comienza a parpadear y el HUD activa un efecto de viñeta roja pulsante. Si la energía llega a 0, la luz se extingue y sobreviene el *Game Over*.
- **Cristales de Luz:** Cada cristal recolectado restaura instantáneamente una porción sustancial de energía (+30 a +35 puntos) e incrementa el contador del nivel.
- **Portal de Salida:** El portal al final de cada nivel permanece bloqueado en un tono apagado hasta que se han recuperado todos los cristales. Al recolectar el último cristal, el portal despierta en un haz brillante cian y permite el paso.

---

## 🕹️ Controles

| Acción | Teclado (Primario) | Teclado (Alternativo) | Mando / Gamepad |
|---|---|---|---|
| **Moverse horizontalmente** | <kbd>A</kbd> / <kbd>D</kbd> | <kbd>←</kbd> / <kbd>→</kbd> | Stick Analógico Izquierdo / D-Pad |
| **Saltar / Aletear (Flutter)** | <kbd>Espacio</kbd> | <kbd>W</kbd> / <kbd>↑</kbd> | Botón Sur (<kbd>A</kbd> en Xbox / <kbd>✕</kbd> en PS) |
| **Planeo sostenido** | Mantener <kbd>Espacio</kbd> | Mantener <kbd>W</kbd> | Mantener Botón Sur |
| **Pausa / Reanudar** | <kbd>Escape</kbd> | <kbd>P</kbd> | Botón Start / Menu |
| **Reintentar Nivel (Game Over)** | <kbd>R</kbd> | <kbd>Enter</kbd> / <kbd>Espacio</kbd> | Botón Sur |

> **Nota sobre el aleteo:** La luciérnaga cuenta con un salto inicial terrestre más **hasta 2 impulsos de aleteo en el aire** antes de requerir posarse nuevamente sobre una plataforma, complementado con amortiguación de caída al sostener la tecla de salto.

---

## 🗺️ Niveles y Curva de Dificultad

El juego incluye **3 niveles jugables** con diseño progresivo:

1. **Nivel 1 - "Cueva Umbría: El Despertar"**
   - *Objetivo:* 3 cristales de luz.
   - *Enfoque:* Introducción intuitiva al aleteo, planeo suave y recarga de luz. Salto guiado sobre un foso de pinchos con un murciélago distante.
2. **Nivel 2 - "El Nido del Eco"**
   - *Objetivo:* 4 cristales de luz.
   - *Enfoque:* Plataformas móviles que cruzan precipicios, 2 murciélagos en pasajes estrechos con ojos rojos brillantes que patrullan en la penumbra.
3. **Nivel 3 - "El Abismo de Cristal"**
   - *Objetivo:* 5 cristales de luz.
   - *Enfoque:* El gran desafío final. Ascenso vertical en caverna profunda, plataformas móviles verticales y horizontales sobre un abismo de pinchos, 3 murciélagos guardianes y un ritmo ajustado de luz hasta el portal hacia la superficie.
4. **Pantalla de Victoria:** Al cruzar el portal del Nivel 3, se presenta la pantalla de celebración con el conteo final de cristales y tiempo total de escape.

---

## 🏗️ Arquitectura de Código (C# y Principios SOLID)

El código sigue estrictamente el **Principio de Responsabilidad Única (SRP)**:

```text
Assets/_Game/Scripts/
├── Audio/
│   └── AudioManager.cs           # Singleton gestor de música ambiental y SFX con variación de tono
├── Core/
│   ├── CameraFollow2D.cs         # Seguimiento suave con SmoothDamp y screen shake en impactos
│   ├── GameInput.cs              # Fachada unificada de entrada compatible con New Input System
│   ├── GameManager.cs            # Singleton persistente para estado global, tiempo y estadísticas
│   └── LevelManager.cs           # Orquestador del flujo por nivel (spawns, cristales, victoria/derrota)
├── Environment/
│   ├── CollectibleCrystal.cs     # Cristal recolectable con animación de levitación, pulso de luz y recarga
│   ├── LevelExit.cs              # Portal de meta con estados bloqueado/activo y disparador de transición
│   └── MovingPlatform.cs         # Plataforma móvil cinemática con fijación suave de pasajeros
├── Hazards/
│   ├── EnemyPatrol.cs            # Murciélago patrullero con vuelo oscilatorio, ojos rojos y daño por contacto
│   ├── HazardSpikes.cs           # Pinchos de cueva con drenaje de energía y retroceso físico
│   └── KillZone.cs               # Límite inferior de caída libre que extingue la luz al caer al vacío
├── Light/
│   └── LightEnergy.cs            # Modelo de energía de luz, escala dinámica de radio/color y alerta crítica
├── Player/
│   └── PlayerController.cs       # Física 2D, aceleración, aleteo aéreo múltiple y detección de suelo
└── UI/
    ├── GameOverUI.cs             # Pantalla de derrota con reinicio rápido por tecla o botón
    ├── MainMenuUI.cs             # Menú principal con modal interactivo de instrucciones y controles
    ├── PauseMenuUI.cs            # Menú de pausa con congelamiento de timeScale y opciones de navegación
    ├── UIManager.cs              # HUD de barra de energía, contador de gemas y viñeta roja crítica
    └── VictoryUI.cs              # Pantalla final con reporte de cristales y tiempo de partida
```

---

## 🛠️ Cómo Abrir y Ejecutar el Proyecto

### Requisitos Previos
- **Unity Hub** instalado.
- **Unity 6000.6.0f1 LTS** (o cualquier versión compatible de Unity 6).

### Pasos para Jugar en el Editor
1. Abre **Unity Hub**.
2. Haz clic en el botón **Add > Add project from disk** y selecciona esta carpeta raíz (`TestMCP`).
3. Abre el proyecto con la versión instalada de Unity 6.
4. En la ventana **Project**, dirígete a `Assets/Scenes/MainMenu.unity` y haz doble clic sobre ella.
5. Pulsa el botón **Play (▶)** en la barra superior de Unity.
6. ¡Disfruta guiando a la luciérnaga a través de la cueva!

### Orden de Escenas en Build Settings
Todas las escenas ya están debidamente configuradas e indexadas en `ProjectSettings/EditorBuildSettings.asset`:
- `[0]` `Assets/Scenes/MainMenu.unity`
- `[1]` `Assets/Scenes/Level1.unity`
- `[2]` `Assets/Scenes/Level2.unity`
- `[3]` `Assets/Scenes/Level3.unity`
- `[4]` `Assets/Scenes/VictoryScene.unity`

---

## 📜 Créditos y Licencias

Todos los sprites, efectos de sonido y pistas musicales han sido creados específicamente para este proyecto y se distribuyen bajo la licencia de dominio público **Creative Commons Zero (CC0 1.0 Universal)**.

Para conocer el detalle de cada archivo y atribución, consulta el archivo [CREDITS.md](CREDITS.md).
