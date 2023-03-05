def my_function():
    huskylens.save_model_to_tf_card(HUSKYLENSMode.SAVE, 0)
buttonClicks.on_button_double_clicked(buttonClicks.AorB.A, my_function)

def on_button_pressed_a():
    global id2
    id2 += 1
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.show_number(id2)
    if id2 > 6:
        id2 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    huskylens.forget_learn()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

id2 = 0
index = 0
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
basic.show_number(id2)

def on_forever():
    if input.button_is_pressed(Button.B):
        huskylens.write_learn1(id2)
basic.forever(on_forever)

def on_forever2():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        music.play_tone(262, music.beat(BeatFraction.HALF))
    else:
        music.play_tone(330, music.beat(BeatFraction.HALF))
basic.forever(on_forever2)
