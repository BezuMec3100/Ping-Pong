from pygame import *
from random import *
font.init()

window = display.set_mode((700, 500))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("tennis.png"),(700, 500))
window.blit(background, (0, 0))

clock = time.Clock()
FPS = 60
run = True

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load (player_image), (75, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.image = transform.scale(image.load (player_image), (30, 100))
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed

player1 = Player("red2.png", 0, 300, 5)
player2 = Player("blue2.png", 670, 300, 5)
ball1 = Gamesprite("ball.png", 400, 300, 5)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    player1.update1()
    player2.update2()
    player1.reset()
    player2.reset()
    ball1.reset()


    display.update()
    clock.tick(FPS)

