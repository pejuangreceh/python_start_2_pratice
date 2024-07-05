from pygame import *
import os
' ' 'Required classes' ' '
# add root dir
script_dir = os.path.dirname(__file__)
print("ini direktori awal == ",script_dir)
# add default image path for bg
image_path = os.path.join(script_dir, 'aset/galaxy.jpg')


#parent class for sprites 
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, width_x, height_y, player_speed):
        super().__init__()
        player_image = os.path.join(script_dir, player_image)
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (width_x, height_y))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y



    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#child class for the player sprite (controlled by arrows)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed

#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Space Shooter")
background = transform.scale(image.load(image_path), (win_width, win_height))

#Game characters:
rocket = Player('aset/rocket.png', 0, win_height - 120,80,120, 4)

game = True
clock = time.Clock()
FPS = 60

#music
# musik diadakan
mixer.init()
# ambil musiknya dari file
mixer.music.load('a-shooting-game/aset/space.ogg')
# mainkan musiknya
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0, 0))
    rocket.reset() 
    rocket.update()
    display.update()
    clock.tick(FPS)

