import random, math, time

WIDTH = 500
HEIGHT = 400

class Animal(Actor):

    all = []

    def __init__(self, id=None):
        super(Animal, self).__init__('sheep.png')
        self.id = id
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.direction = random.uniform(0, math.pi * 2)
        self.speed = random.uniform(2,4)

        Animal.all.append(self)

    def move(self):
        # Our default direction vector
        dx = 0 #math.cos(self.direction) * self.speed
        dy = 0 #math.sin(self.direction) * self.speed

        # Change our direction and speed according to other animals
        for o in self.other_animals():
            angle = self.angle_to(o)
            fx = math.cos(angle) * self.attraction_to(o)
            fy = math.sin(angle) * self.attraction_to(o)
            #print(self.id, o.id, angle, (fx, fy))

            dx += fx
            dy += fy

        self.x += dx
        self.y += dy

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
        # Attraction gets stronger the closer the other gets
        d = self.distance_to(other)
        if d > 50:
            return min(2, 30 / d)
        else:
            return -min(2, 10 / d)

# Make 3 animals
Animal(1)
Animal(2)
Animal(3)
Animal(1)
Animal(2)
Animal(3)

def draw():
    screen.clear()
    for a in Animal.all: a.draw()
    #time.sleep(2)

def update():
    for a in Animal.all: a.move()