from pygame import *
from random import randint
FPS = 60
window_size = 1200,600
init() 
running = True
lose = False

screen = display.set_mode(window_size)
clock = time.Clock()

class Bird:
    def __init__(self,x,y,img=None):
        self.x = x
        self.y = y
        self.img = img
        if self.img:
            self.rect = self.img.get_rect()
        else:
            self.rect = Rect(self.x,self.y,100,100)
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -=3
        if keys[K_DOWN]:
            self.rect.y +=3
    def draw(self):
        if self.img:
            screen.blit(self.img,self.rect)
        else:
            draw.rect(screen,"red",self.rect)

class Tube:
    def __init__(self,x,y,width = 120,height = 600,img = None    ):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        if self.img:
            self.rect = self.img.get_rect()
        else:
            self.rect = Rect(self.x,self.y,width,height)
    def update(self):
        self.rect.x -= 3
    def draw(self):
        if self.img:
            screen.blit(self.img,self.rect)
        else:
            draw.rect(screen,"green",self.rect)

def generate_tubes(count):
    xcor = 1200
    tubes = list()

    for i in range(count):
        ycor = randint(-700,-200)
        top_tube = Tube(xcor,ycor)
        bottom_tube = Tube(xcor,ycor + 100 + 800)
        xcor += 600
        tubes.extend((top_tube,bottom_tube))
    return tubes

bird = Bird(100,100)
tubes = generate_tubes(6)
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    screen.fill("skyblue")
    bird.update()
    for t in tubes:
        t.update()
        t.draw()
    bird.draw()
    display.update()
    clock.tick(FPS)