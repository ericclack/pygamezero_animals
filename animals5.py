import random, math, time
from enum import Enum
import pygame
from animals_lib import *

WIDTH = 800
HEIGHT = 800
MAX_SPEED = 2

class Status(Enum):
    DEAD = 0
    ALIVE = 1

class Animal(Actor):

    # Collect all the animals
    all = []

    def __init__(self, img):
        super(Animal, self).__init__(img)
        self.status = Status.ALIVE
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.direction = random.uniform(0, math.pi * 2)
        self.max_speed = MAX_SPEED
        self.speed = random.uniform(0.05, self.max_speed)

        Animal.all.append(self)

    def move(self, check_animals=True, check_zones=True, check_mouse=False):
        if self.status == Status.DEAD:
            return

        # Our default direction vector
        dx, dy = xy_from_angle_mag(self.direction, self.speed)

        # Change our direction and speed according to other animals
        if check_animals:
            for o in self.other_animals():
                fx, fy = xy_from_angle_mag(self.angle_to(o), self.attraction_to(o))
                dx += fx
                dy += fy

        # Check no-go zones
        if check_zones:
            for z in Zone.all:
                fx, fy = xy_from_angle_mag(self.angle_to(z), z.attraction_to(self))
                dx += fx
                dy += fy

        if check_mouse:
            mx, my = pygame.mouse.get_pos()
            angle, mag = angle_mag_from_xy(mx - self.x, my - self.y)
            fx, fy = xy_from_angle_mag(angle, self.attraction_to_mouse(mag))
            dx += fx
            dy += fy

        # Uptdate direction with attractions above
        self.direction, self.speed = angle_mag_from_xy(dx, dy)
        # Don't move too fast
        self.speed = min(self.max_speed, self.speed)
        # Create the actual movement vector given that we might have reduced speed
        dx, dy = xy_from_angle_mag(self.direction, self.speed)

        # Move
        self.x += dx
        self.y += dy

        self.wrap_around()

    def wrap_around(self):
        if self.x < 0:         self.x = WIDTH
        elif self.x > WIDTH:   self.x = 0
        if self.y < 0:         self.y = HEIGHT
        elif self.y > HEIGHT:  self.y = 0

    def other_animals(self):
        """All the animals except us"""
        return [a for a in Animal.all if a != self]

    def distance_to(self, other):
        # Pythagoras
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def angle_to(self, other):
        # 0 is left, pi/2 is up, pi is right, -pi/2 down
        return math.atan2(other.y - self.y, other.x - self.x)

    def attraction_to(self, other):
        # No attraction by default
        return 0


class Zone():

    all = []
    SAFE = (0, 150, 150)
    NO_GO = (150, 0, 0)

    def __init__(self, x, y, size, ztype):
        self.x = x
        self.y = y
        self.size = size
        self.ztype = ztype

        Zone.all.append(self)

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.size // 2, self.ztype)

    def attraction_to(self, a):
        """How attractive is this zone to this animal?"""
        distance = a.distance_to(self)
        from_edge = distance - self.size // 2

        if self.ztype == Zone.NO_GO:
            if from_edge <= 0: return -100

        if self.ztype == Zone.SAFE and isinstance(a, Wolf):
            if from_edge <= 0: return -100

        return 0

# ----------------------------------------------------------

class Sheep(Animal):
    def __init__(self):
        super().__init__('sheep.png')
        self.max_speed = 1

    def attraction_to(self, other):
        """Positive number means attraction, negative repulsion"""
        d = self.distance_to(other)

        # Attraction gets stronger the closer we get to other sheep, unless
        # we get too close
        if isinstance(other, Sheep) and other.status == Status.ALIVE:
            if d > 50: return 5 / (d / 5) ** 2
            else:      return -5 / d

        elif isinstance(other, Wolf):
            # A wolf, run away!
            return -15 / (d / 10) ** 2

        elif isinstance(other, SheepDog):
            return -10 / (d / 5) ** 2

        return 0

class Wolf(Animal):
    def __init__(self):
        super().__init__('wolf.png')
        self.max_speed = MAX_SPEED*1.5

    def move(self):
        super().move()
        others = self.other_animals()

        # Caught a sheep?
        i = self.collidelist(others)
        if i != -1 and isinstance(others[i], Sheep):
            others[i].status = Status.DEAD

    def attraction_to(self, other):
        # Attraction gets stronger the closer the other gets
        d = self.distance_to(other)
        if isinstance(other, Sheep):
            if other.status == Status.DEAD:
                return 0
            else:
                return 15 / (d / 10) ** 2

        if isinstance(other, SheepDog):
            return -15 / (d/20) ** 2

class SheepDog(Animal):
    def __init__(self):
        super().__init__('dog.png')
        self.max_speed = MAX_SPEED*1.4

    def move(self):
        super().move(check_animals=False, check_zones=True, check_mouse=True)

    def attraction_to_mouse(self, distance):
        return 1


# Make animals
for i in range(20):
    Sheep()
Wolf()
SheepDog()

# Make zones
Zone(150, 150, 450, Zone.SAFE)

Zone(WIDTH/2, HEIGHT/2, 200, Zone.NO_GO)
Zone(WIDTH/2 + 75, HEIGHT/2 - 75, 100, Zone.NO_GO)
Zone(WIDTH/2 + 150, HEIGHT/2 - 150, 100, Zone.NO_GO)
Zone(WIDTH/2 - 75, HEIGHT/2 + 75, 100, Zone.NO_GO)

def draw():
    screen.clear()
    for z in Zone.all: z.draw()
    for a in Animal.all: a.draw()

def update():
    for a in Animal.all: a.move()