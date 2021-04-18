import random

WIDTH = 600
HEIGHT = 400
TITLE = "Animal Simulation"

class Animal(Actor):

    def __init__(self):
        super().__init__('sheep.png')
        self.x = random.randint(WIDTH*1/4, WIDTH*3/4)
        self.y = random.randint(HEIGHT*1/4, HEIGHT*3/4)

    def move(self):
        self.x += 1
        self.y += 0.5

a = Animal()

def draw():
    screen.blit('southdowns.jpeg', (0,0))
    a.draw()

def update():
    a.move()