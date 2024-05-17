from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Catch")
background = transform.scale(image.load("background.png"), (700, 500))

window.blit(background,(0, 0))
