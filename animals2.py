import random, math, time

WIDTH = 500
HEIGHT = 400
MAX_SPEED = 4

class Animal(Actor):

    all = []

    def __init__(self, what):
        super(Animal, self).__init__('%s.png' % what)
        self.what = what
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.direction = random.uniform(0, math.pi * 2)
        self.max_speed = MAX_SPEED
        self.speed = random.uniform(2,self.max_speed)


        Animal.all.append(self)

    def move(self):
        # Our default direction vector
        dx = math.cos(self.direction) * self.speed
        dy = math.sin(self.direction) * self.speed

        # Change our direction and speed according to other animals
        for o in self.other_animals():
            angle = self.angle_to(o)
            fx = math.cos(angle) * self.attraction_to(o)
            fy = math.sin(angle) * self.attraction_to(o)

            dx += fx
            dy += fy

        # Uptdate direction with attractions above
        self.speed = min(self.max_speed, math.sqrt(dx ** 2 + dy ** 2))
        self.direction = math.atan2(dy, dx)

        self.x += dx
        self.y += dy

        if self.x < 0 or self.y < 0 or self.x > WIDTH or self.y > HEIGHT:
            self.direction += math.pi

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
        0 # No attraction by default

class Sheep(Animal):
    def __init__(self): super(Sheep, self).__init__('sheep')

    def attraction_to(self, other):
        d = self.distance_to(other)

        # Attraction gets stronger the closer we get to other sheep
        if other.what == 'sheep':
            if d > 50:
                return 5 / d
            else:
                return -5 / d

        elif other.what == 'wolf':
            # A wolf, run away!
            return -25 / d

class Wolf(Animal):
    def __init__(self):
        super(Wolf, self).__init__('wolf')
        self.chasing = random.choice(self.other_animals())

    def move(self):
        super(Wolf, self).move()
        others = self.other_animals()
        i = self.collidelist(others)
        if i != -1 and others[i].what == 'sheep':
            others[i].max_speed = 0.1

    def attraction_to(self, other):
        # Attraction gets stronger the closer the other gets
        d = self.distance_to(other)
        if other.what == 'sheep':
            if other == self.chasing:
                return 15 / d
            else:
                return 10 / d

# Make animals
for i in range(20):
    Sheep()
Wolf()

def draw():
    screen.clear()
    for a in Animal.all: a.draw()
    #time.sleep(2)

def update():
    for a in Animal.all: a.move()