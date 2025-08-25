fractionQuestion = 0

def on_button_pressed_a():
    global fractionQuestion
    fractionQuestion = Math.random_range(1, 3)
    if fractionQuestion == 1:
        basic.show_string("1/2 + 1/4 = ?")
    elif fractionQuestion == 2:
        basic.show_string("2/3 - 1/3 = ?")
    elif fractionQuestion == 3:
        basic.show_string("3/4 * 1/2 = ?")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if fractionQuestion == 1:
        basic.show_number(1 / 2 + 1 / 4)
    elif fractionQuestion == 2:
        basic.show_number(2 / 3 - 1 / 3)
    elif fractionQuestion == 3:
        basic.show_number(3 / 4 * 1 / 2)
input.on_button_pressed(Button.B, on_button_pressed_b)
