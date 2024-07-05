#create a Maze game!

from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))

display.set_caption("Maze")

background = transform.scale(image.load("games2/background.jpg",),(700,500))
game = True
while game: 
    window.blit(background,(win_width,win_height))
    for e in event.get():
       if e.type == QUIT:
            game = False
    display.update()