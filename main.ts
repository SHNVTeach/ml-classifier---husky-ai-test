input.onButtonPressed(Button.A, function () {
    id += 1
    basic.showNumber(id)
    if (id > 6) {
        id = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    huskylens.forgetLearn()
})
let id = 0
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.OBJECTCLASSIFICATION)
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
huskylens.writeName(0, "Blue")
huskylens.writeName(1, "Plain Shirt")
huskylens.writeName(2, "Nothing")
huskylens.writeName(3, "Dress")
huskylens.writeName(4, "Face")
huskylens.writeName(5, "Pants")
huskylens.writeName(6, "Pattern Shirt")
id = 0
let index = 0
basic.showNumber(id)
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        huskylens.writeLearn1(id)
    }
})
