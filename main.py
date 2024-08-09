from pygame import *
import math
import random

debug = False
wrapmode = True #does the player wrap around the edges?

res = (700, 500)
FPS = 60
BPS = 6 #bullets per second

FPB = FPS/BPS #frames per bullet


window = display.set_mode(res)
display.set_caption("pong")

def drawtext(text, x, y, size = 20, color = (255,255,255)):
    font.init()
    f = font.Font(None, size)
    window.blit(f.render(text, True, color), (x,y))

def lerp(a,b,t):
    return a + (t * (b-a))

class Sprite(sprite.Sprite): #handles pygame image rendering
    def __init__(self, img, x, y, w, h, dx = 0, dy = 0):
        '''image : image path'''
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = dx
        self.dy = dy
    
    def render(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, w, h, img, controls = [K_w, K_s]):
        super().__init__(img, x, y, w, h)

        self.dx = 0
        self.dy = 0
        #movement speed
        self.speed = 120
        self.controls = controls
    
    def update(self, keys):

        #friction
        self.dx *= 0.7
        self.dy *= 0.7

        movedir = (0,0)
        if keys[self.controls[0]]:
            movedir = (movedir[0], movedir[1] - 1)
        if keys[self.controls[1]]:
            movedir = (movedir[0], movedir[1] + 1)

        self.dx += movedir[0] * self.speed / FPS
        self.dy += movedir[1] * self.speed / FPS

        
        #if abs(self.dx) < 0.001: self.dx = 0
        #if abs(self.dy) < 0.001: self.dy = 0

        #looping

        self.rect.x += self.dx
        self.rect.y += self.dy
        if wrapmode: self.rect.x = (self.rect.x + 70) % 770 - 70



bg = Sprite("galaxy.jpg", 0, 0, res[0], res[1])
clock = time.Clock()
game = True
active = True

p1 = Player(20, res[1]/2 - 75, 30, 150, "pedal.png", [K_w, K_s])
p2 = Player(res[0]-60, res[1]/2 - 75, 30, 150, "pedal.png", [K_o, K_l])

while active:
    if game:
        keys = key.get_pressed()
        p1.update(keys)
        p2.update(keys)

        bg.render()
        p1.render()
        p2.render()

    for e in event.get():
        if e.type == QUIT:
            active = False
    clock.tick(FPS)
    display.update()
