from pygame import *
import os
import random

# add root dir
script_dir = os.path.dirname(__file__)
print("ini direktori awal == ",script_dir)

#background music
mixer.init()
mixer.music.load('shoot/space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('shoot/fire.ogg')

#fonts and labels
font.init()
font2 = font.Font(None, 36)

# we need these pictures:
img_back = "galaxy.jpg" # game background
img_hero = "rocket.png" # character
img_alien = "ufo.png" # character

# tambahkan os
img_back = os.path.join(script_dir, img_back)
img_hero = os.path.join(script_dir, img_hero)
img_alien = os.path.join(script_dir, img_alien)

# variabel untuk skor dan lost
score = 0
missed = 0

# parent class for other sprites
class GameSprite(sprite.Sprite):
  # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # We call the class constructor (Sprite):
        sprite.Sprite.__init__(self)

        # each sprite must store an image property
        player_image = os.path.join(script_dir, player_image)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # method that draws the character in the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# main player class
class Player(GameSprite):
    # method for controlling the sprite with keyboard arrows
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
  # the "fire" method (use the player's place to create a bullet there)
    def fire(self):
        pass

class Monster(GameSprite):
    # method for controlling the sprite with keyboard arrows
    
    def update(self):
        global missed
        # jika posisi y masih dibawah 500 maka arahnya "down"
        if self.rect.y <= 500:
            self.side = "down"
        # jika tidak, maka arahnya menjadi "restart" 
        else:
            self.side = "restart"

        # jika arahnya down, maka koordinat akan ditambah terus menerus
        if self.side == "down":
            self.rect.y += self.speed
        else:
            self.rect.x = random.randint(100,600)
            self.rect.y = 0
            missed += 1
         

# Create the window
win_width = 700
win_height = 500



display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# create sprites
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

# create alien
aliens = sprite.Group()
for i in range(1,6):
    speed_random = random.randint(1,8)
    print("alien ke ",i, "kecepatan = ",speed_random )
    alien = Monster(img_alien, random.randint(100,600), 0, 100, 60, speed_random)
    aliens.add(alien)

# the "game over" variable: as soon as it is True, the sprites stop working in the main loop
finish = False
# Main game loop:
run = True # the flag is cleared with the close window button
while run:
    # the press the Close button event
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        # refresh background
        window.blit(background,(0,0))

        # producing sprite movements
        ship.update()
        aliens.update()

        text = font2.render("Score: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        
        text = font2.render("Missed: " + str(missed), 1, (255, 255, 255))
        window.blit(text, (10, 50))

        # updating them at a new location on each iteration of the loop
        ship.reset()
        # aliens.reset()
        aliens.draw(window)

        display.update()
    # the loop runs every 0.05 seconds
    time.delay(50)
