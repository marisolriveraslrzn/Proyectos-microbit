def detectar_movimiento():
    if input.acceleration(Dimension.STRENGTH) > 1500:
        basic.show_icon(IconNames.SURPRISED)
        music.play_tone(Note.C, music.beat(BeatFraction.HALF))
    else:
        basic.clear_screen()

basic.forever(detectar_movimiento)
