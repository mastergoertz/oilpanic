input.onButtonPressed(Button.A, function () {
    music.playTone(262, music.beat(BeatFraction.Quarter))
    if (x_pos > 0) {
        led.unplot(x_pos - 1, 4)
        x_pos = 0
        led.plot(x_pos, 4)
    }
})
function inc_bomb () {
    led.unplot(bomb_x, bomb_y)
    if (bomb_y < 4) {
        bomb_y += 1
    }
    led.plot(bomb_x, bomb_y)
}
input.onButtonPressed(Button.B, function () {
    music.playTone(262, music.beat(BeatFraction.Quarter))
    if (x_pos < 4) {
        led.unplot(x_pos, 4)
        x_pos = x_pos + 1
        led.plot(x_pos, 4)
    }
})
function reset_game () {
    basic.clearScreen()
    count = 0
    speed = 500
    x_pos = 2
    bomb_x = randint(0, 4)
    bomb_y = 0
    led.plot(x_pos, 4)
    led.plot(bomb_x, bomb_y)
}
let speed = 0
let count = 0
let bomb_y = 0
let bomb_x = 0
let x_pos = 0
reset_game()
basic.forever(function () {
    basic.pause(500)
    inc_bomb()
    if (bomb_x != x_pos && bomb_y == 4) {
        soundExpression.sad.play()
        for (let index = 0; index < 4; index++) {
            basic.showIcon(IconNames.Skull)
            basic.pause(200)
            basic.clearScreen()
            basic.pause(200)
        }
        reset_game()
    }
    if (bomb_y == 4) {
        reset_game()
        music.playTone(659, music.beat(BeatFraction.Quarter))
    }
})
