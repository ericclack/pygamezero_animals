import random, math, time

WIDTH = 500
HEIGHT = 400

class Animal(Actor):

    all = []

    def __init__(self):
        super(Animal, self).__init__('sheep.png')
        self.x = random.randint(WIDTH*1/5, WIDTH*4/5)
        self.y = random.randint(HEIGHT*1/5, HEIGHT*4/5)
        Animal.all.append(self)

    def move(self):
        for o in self.other_animals():
            self.move_by_attraction(o)

        # Wrap around
        if self.x < 0:         self.x = WIDTH
        elif self.x > WIDTH:   self.x = 0
        if self.y < 0:         self.y = HEIGHT
        elif self.y > HEIGHT:  self.y = 0

    def other_animals(self):
        """All the animals except us"""
        return [a for a in Animal.all if a != self]

    def move_by_attraction(self, other):
        angle = self.angle_to(other)
        fx = math.cos(angle) * self.attraction_to(other)
        fy = math.sin(angle) * self.attraction_to(other)
        self.x += fx
        self.y += fy

    def distance_to(self, other):
        # Distances
        dx = self.x - other.x
        dy = self.y - other.y
        # Pythagoras
        return math.sqrt(dx**2 + dy**2)

    def angle_to(self, other):
        # 0 is left, pi/2 is up, pi is right, -pi/2 down
        return math.atan2(other.y - self.y, other.x - self.x)

    def attraction_to(self, other):
        # Attraction until we get too close
        d = self.distance_to(other)
        return min(0.25, (-30/d) + 0.01*d)

# Make 3 animals
Animal()
Animal()
Animal()
Animal()
Animal()
Animal()

def draw():
    screen.blit('southdowns.jpeg', (0,0))
    for a in Animal.all: a.draw()

def update():
    for a in Animal.all: a.move()