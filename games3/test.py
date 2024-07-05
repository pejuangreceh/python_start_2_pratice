from pygame import *
import os
' ' 'Required classes' ' '
# add root dir
script_dir = os.path.dirname(__file__)
print("ini direktori awal == ",script_dir)
# add default image path for bg
image_path = os.path.join(script_dir, 'background.jpg')
print("ini direktori background == ",image_path)


#parent class for sprites 
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        player_image = os.path.join(script_dir, player_image)
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y



    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



# child class
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
        
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        # print("cek data x monster ",self.rect.x)
        if self.rect.x <= 470:
            self.direction = "right"
            # print("ganti arah ke kanan")
        if self.rect.x >= win_width - 85: # kalo lebih dari 615
            self.direction = "left"
            # print("ganti arah ke kiri")

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load(image_path), (win_width, win_height))

#Game characters:
packman = Player('hero.png', 100, win_height - 500, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)#620
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)


game = True
clock = time.Clock()
FPS = 60

#music
# musik diadakan
mixer.init()
# ambil musiknya dari file
mixer.music.load('games3/jungles.ogg')
# mainkan musiknya
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(background,(0, 0))
    packman.update()
    monster.update()

    packman.reset() #window.blit(self.image, (self.rect.x, self.rect.y))
    monster.reset() #window.blit(self.image, (self.rect.x, self.rect.y))
    final.reset()   #window.blit(self.image, (self.rect.x, self.rect.y))

    display.update()
    clock.tick(FPS)

