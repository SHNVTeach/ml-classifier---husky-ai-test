buttonClicks.onButtonDoubleClicked(buttonClicks.AorB.A, function () {
    huskylens.saveModelToTFCard(HUSKYLENSMode.SAVE, 0)
})
input.onButtonPressed(Button.A, function () {
    id += 1
    basic.showNumber(id)
    if (id > 5) {
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
huskylens.writeName(0, "Background")
huskylens.writeName(1, "T-Shirt")
huskylens.writeName(2, "Pants")
huskylens.writeName(3, "Dress")
huskylens.writeName(4, "Face")
huskylens.writeName(5, "Pattern Shirt")
id = 0
basic.showNumber(id)
basic.forever(function () {
    if (input.buttonIsPressed(Button.B)) {
        huskylens.writeLearn1(id)
    }
})
basic.forever(function () {
    huskylens.request()
    if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
        basic.showString("1")
    }
})
