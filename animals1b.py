import random

WIDTH = 500
HEIGHT = 400
TITLE = "Animal Simulation"

class Animal(Actor):

    all = []

    def __init__(self):
        super().__init__('sheep.png')
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.xspeed = random.uniform(-1,1)
        self.yspeed = random.uniform(-1,1)
        Animal.all.append(self)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed


Animal()
Animal()
Animal()

def draw():
    screen.clear()
    for a in Animal.all: a.draw()

def update():
    for a in Animal.all: a.move()
