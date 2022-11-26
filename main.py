def on_button_pressed_a():
    global id2
    id2 += 1
    basic.show_number(id2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    huskylens.forget_learn()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

id2 = 0
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.OBJECTCLASSIFICATION)
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
huskylens.write_name(0, "Blue")
huskylens.write_name(1, "Plain Shirt")
huskylens.write_name(2, "Nothing")
huskylens.write_name(3, "Dress")
huskylens.write_name(4, "Face")
huskylens.write_name(5, "Pants")
huskylens.write_name(6, "Pattern Shirt")
id2 = 0

def on_forever():
    if input.button_is_pressed(Button.B):
        huskylens.write_learn1(id2)
basic.forever(on_forever)
