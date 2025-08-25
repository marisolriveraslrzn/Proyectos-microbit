# 🧠 Proyectos Educativos con micro:bit

Este repositorio reúne una colección de proyectos interactivos desarrollados con [Microsoft MakeCode para micro:bit](https://makecode.microbit.org/#editor). Están diseñados para fomentar el aprendizaje STEAM mediante actividades visuales, gamificadas y accesibles para distintos niveles educativos.

## 🎯 Objetivos del repositorio
- Promover la enseñanza de programación y electrónica básica con micro:bit.
- Compartir actividades didácticas aplicables en entornos escolares y talleres.
- Documentar cada proyecto con ejemplos, simulaciones y recursos visuales.
- Facilitar la integración de micro:bit en portafolios educativos internacionales.

## 🧭 Compatibilidad y versiones

Este repositorio incluye proyectos compatibles con distintas versiones de la placa BBC micro:bit:

| Versión de placa | Compatibilidad | Entorno recomendado | Lenguaje | Simulador |
|------------------|----------------|----------------------|----------|-----------|
| micro:bit V1     | ✅             | MakeCode / Python    | Blocks / Python | Sí |
| micro:bit V2     | ✅             | MakeCode / Python    | Blocks / Python | Sí |
| micro:bit V2.2+  | ⚠️ Parcial     | MakeCode (beta)      | Blocks / Python | Limitado |

> ⚠️ Algunos proyectos pueden requerir ajustes según la versión de placa. Se recomienda verificar el modelo antes de cargar el código.

### 📦 Versionado del repositorio

- **Versión actual**: `v0.1.0` – Inicio del repositorio con proyectos básicos y juegos.
- **Próxima versión**: `v0.2.0` – Inclusión de proyectos musicales, sensores y documentación extendida.
- **Historial de cambios**: disponible en el archivo `CHANGELOG.md`.
## 🧪 Ejemplo destacado

**🔊 Clap Lights (Luces por aplauso)**  
Detecta sonidos fuertes y enciende una animación LED. Ideal para enseñar eventos, condicionales y sensores.

```python
def on_sound_loud():
    global lighsOn
    lighsOn = not (lighsOn)
    if lighsOn:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
        """)
    else:
        basic.clear_screen()

input.on_sound(DetectedSound.LOUD, on_sound_loud)
lighsOn = False
input.set_sound_threshold(SoundThreshold.LOUD, 150)

```

## 🧰 Herramientas utilizadas
- MakeCode Editor para bloques, Python y simulaciones.
- micro:bit v2 para pruebas físicas.
- GitHub para documentación y colaboración.

## 📚 Recursos complementarios
- Guías paso a paso en cada carpeta.
- Archivos ,py para guia de código(no confundir con .HEX).

## 🧵 Contribuciones
Este repositorio está abierto a docentes, estudiantes y entusiastas de la programación educativa. Puedes:

- Proponer nuevos proyectos.
- Mejorar la documentación.
- Traducir actividades o adaptarlas a otros niveles.

---

🪪 Licencia
© Marisol Rivera Solórzano
- Contenido educativo distribuido bajo licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).  
Se permite su uso y adaptación con atribución, sin fines comerciales y compartiendo bajo la misma licencia.

---


