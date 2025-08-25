from microbit import *
import random

# Lista de opciones
opciones = ["Piedra", "Papel", "Tijera"]

# Íconos personalizados
iconos = {
    "Piedra": Image("09990:99999:99999:09990:00900"),
    "Papel": Image("99999:90009:90009:90009:99999"),
    "Tijera": Image("99099:99099:00900:09990:09990")
}

while True:
    if accelerometer.was_gesture("shake"):
        opcion = random.choice(opciones)
        display.show(iconos[opcion])
        sleep(2000)
        display.clear()
