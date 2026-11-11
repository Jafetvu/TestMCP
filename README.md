# Luciérnaga (Firefly) - 2D Dark Cave Exploration

**Luciérnaga** es un videojuego de plataformas y exploración 2D desarrollado en **Unity 6 (6000.6.0f1)** con el **Universal Render Pipeline (URP 2D)**.

El jugador controla una pequeña luciérnaga atrapada en cavernas profundas y oscuras. La luz que emite es su mayor defensa y su propia vida: se agota continuamente con el tiempo y solo puede recargarse recolectando cristales de luz ancestrales esparcidos por la cueva. Si la luz se apaga por completo, la oscuridad consume a la luciérnaga.

---

## 🎮 Características principales

- **Mecánica de Luz Dinámica (URP 2D Lights):** La luz del jugador ilumina un radio limitado de la caverna. A medida que la energía disminuye, el radio y la intensidad de la luz decrecen, aumentando la tensión.
- **Exploración por Niveles:** 3 niveles con diseño y dificultad progresiva.
- **Objetivo de Nivel:** Recolecta todos los cristales de luz para reactivar el portal de salida y avanzar.
- **Peligros y Obstáculos:**
  - Murciélagos de cueva que patrullan la oscuridad.
  - Pinchos y estalagmitas afiladas.
  - Plataformas móviles para cruzar abismos oscuros.
- **Interfaz completa:** Menú principal, HUD en tiempo real (barra de luz y contador de cristales), pantalla de pausa, Game Over y Pantalla de Victoria.
- **Audio integrado:** Efectos sonoros y ambiente sonoro para sumergir al jugador en la atmósfera de la cueva.

---

## 🕹️ Controles

| Acción | Teclado (Primario) | Teclado (Alternativo) | Mando / Gamepad |
|---|---|---|---|
| Moverse horizontalmente | **A / D** | Flechas Izq. / Der. | Stick Izquierdo / D-Pad |
| Saltar / Aletear | **Espacio** | W / Flecha Arriba | Botón Sur (A / Cruz) |
| Pausa | **Escape** | P | Botón Start / Menu |
| Reintentar (Game Over) | **R** | Espacio / Enter | Botón Sur |

---

## 📁 Estructura del Proyecto

```text
Assets/
├── _Game/
│   ├── Audio/          # Efectos de sonido y música ambiental
│   ├── Materials/      # Materiales y shaders URP 2D
│   ├── Prefabs/        # Prefabs de jugador, enemigos, cristales, portales, UI
│   ├── Scenes/         # Escenas: Menú, Niveles 1-3, Victoria
│   ├── Scripts/
│   │   ├── Audio/      # AudioManager y disparadores de sonido
│   │   ├── Core/       # GameManager, LevelManager
│   │   ├── Environment/# Cristales, Plataformas móviles, Portales de salida
│   │   ├── Hazards/    # Murciélagos patrulleros, Pinchos
│   │   ├── Light/      # Gestión de energía de luz y radio 2D
│   │   ├── Player/     # Control de movimiento 2D y física
│   │   └── UI/         # HUD, Menú Principal, Pausa, Game Over, Victoria
│   └── Sprites/        # Sprites minimalistas 2D generados para el juego
├── Scenes/             # Escenas principales del juego
└── Settings/           # Configuración de URP 2D e Input System
```

---

## 🛠️ Requisitos e Instrucciones de Ejecución

1. **Versión de Unity recomendada:** `Unity 6000.6.0f1` (o cualquier versión compatible de Unity 6 LTS) con soporte URP 2D y New Input System.
2. **Cómo abrir el proyecto:**
   - Abre **Unity Hub**.
   - Haz clic en **Add > Add project from disk** y selecciona esta carpeta raíz.
   - Abre el proyecto con Unity 6000.6.0f1.
3. **Cómo jugar:**
   - En la ventana del *Project*, navega a `Assets/Scenes/MainMenu.unity` (o `Level1.unity`).
   - Pulsa el botón **Play** en el Editor de Unity.
