# 🔊 Luces por aplauso

Este proyecto utiliza la placa micro:bit para detectar sonidos fuertes (como un aplauso) y encender una animación LED. Es ideal para introducir conceptos como sensores, eventos y condicionales en programación educativa.

## 🧠 ¿Qué aprende el estudiante?

- Uso de sensores de sonido.
- Programación de eventos (`on_sound_loud`).
- Condicionales y lógica booleana.
- Visualización con matriz LED.

## 🖼 Simulador 
![Simulación del proyecto](../../Images/Imag1.jpeg)

## 🎬 ¿Qué hace el proyecto?

Cuando el micro:bit detecta un sonido fuerte (como un aplauso), alterna entre mostrar una figura en la matriz LED y apagarla. Es una forma divertida de enseñar interacción física con el entorno.

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
