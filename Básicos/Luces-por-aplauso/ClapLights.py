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
