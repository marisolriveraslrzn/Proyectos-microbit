tool = 0

def on_gesture_shake():
    global tool
    tool = randint(0, 2)
    if tool == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif tool == 1:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
