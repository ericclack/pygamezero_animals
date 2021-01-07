import random

WIDTH = 500
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
    a.draw()

def update():
    a.move()