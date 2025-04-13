from pygame import *
init()

clock = time.Clock()
#Початкові налаштування
WINDOW_SIZE = (700, 500)
SPRITE_SIZE = (65, 65)
FPS = 60

window = display.set_mode(WINDOW_SIZE)
display.set_caption("Догонялки")
#window.fill((15, 58, 32))
background = transform.scale(image.load("background.png"), WINDOW_SIZE)
sprite1 = transform.scale(image.load("sprite1.png"), SPRITE_SIZE)
sprite2 = transform.scale(image.load("sprite2.png"), SPRITE_SIZE)


x1, y1 = 50, 50
x2, y2 = 50, 50
#Ігровий цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    keys = key.get_pressed()

    if keys[K_w] and y1 > 0:
        y1 -= 10
    if keys[K_s] and y1 < WINDOW_SIZE[1] - SPRITE_SIZE[1]:
        y1 += 10
    if keys[K_a] and x1 > 0:
        x1 -= 10
    if keys[K_d] and x1 < WINDOW_SIZE[0] - SPRITE_SIZE[0]:
        x1 += 10

    if keys[K_UP] and y2 > 0:
        y2 -= 10
    if keys[K_DOWN] and y2 < WINDOW_SIZE[1] - SPRITE_SIZE[1]:
        y2 += 10
    if keys[K_LEFT] and x2 > 0:
        x2 -= 10
    if keys[K_RIGHT] and x2 < WINDOW_SIZE[0] - SPRITE_SIZE[0]:
        x2 += 10





    display.update()
    clock.tick(FPS)