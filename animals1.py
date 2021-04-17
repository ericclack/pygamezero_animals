import random

WIDTH = 600
HEIGHT = 400
TITLE = "Animal Simulation"

class Animal(Actor):

    def __init__(self):
        super().__init__('sheep.png')
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

    def move(self):
        self.x += 1
        self.y += 0.5

a = Animal()

def draw():
    screen.blit('southdowns.jpeg', (0,0))
    a.draw()

def update():
    a.move()