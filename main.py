def on_button_pressed_a():
    global x_pos
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    if x_pos > 0:
        led.unplot(x_pos, 4)
        x_pos = x_pos - 1
        led.plot(x_pos, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def inc_bomb():
    global bomb_y
    led.unplot(bomb_x, bomb_y)
    if bomb_y < 4:
        bomb_y += 1
    led.plot(bomb_x, bomb_y)

def on_button_pressed_b():
    global x_pos
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    if x_pos < 4:
        led.unplot(x_pos, 4)
        x_pos = x_pos + 1
        led.plot(x_pos, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def reset_game():
    global count, speed, x_pos, bomb_x, bomb_y
    basic.clear_screen()
    count = 0
    speed = 500
    x_pos = 2
    bomb_x = randint(0, 4)
    bomb_y = 0
    led.plot(x_pos, 4)
    led.plot(bomb_x, bomb_y)
speed = 0
count = 0
bomb_y = 0
bomb_x = 0
x_pos = 0
reset_game()

def on_forever():
    basic.pause(500)
    inc_bomb()
    if bomb_x != x_pos and bomb_y == 4:
        soundExpression.sad.play()
        for index in range(4):
            basic.show_icon(IconNames.SKULL)
            basic.pause(200)
            basic.clear_screen()
            basic.pause(200)
        reset_game()
    if bomb_y == 4:
        reset_game()
        music.play_tone(659, music.beat(BeatFraction.QUARTER))
basic.forever(on_forever)
