from pygame import *

window = display.set_mode((700,500))

display.set_caption("Catch")
background = transform.scale(image.load("games/background.png"),(700,500))

sprite1 = transform.scale(image.load("games/sprite1.png"),(100,100))
sprite2 = transform.scale(image.load("games/sprite2.png"),(100,100))

clock = time.Clock()
FPS = 60

x1 = 100
y1 = 100
speed = 10
x2 = 200
y2 = 200

game = True
while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    key_pressed = key.get_pressed()
    if key_pressed[K_UP] and y1 > 0:
        y1 -= speed 
    if key_pressed[K_DOWN] and y1 < 400:
        y1 += speed
    if key_pressed[K_RIGHT]and x1 < 600:
        x1 += speed
    if key_pressed[K_LEFT]and x1 > 0:
        x1 -= speed
    display.update()
    clock.tick(FPS)
