.. _part3:

Part 3
======

So let's add a sheep dog so that we can try and herd the sheep
and explore forces of fear as well as attraction.

New kinds of Animal
-------------------

At the moment we have one new class `Animal` which represents our
sheep, so we're going to create two new kinds of animal, one for the
sheep and one for the sheep dog.

Do you remember when we created the `Animal` class we said it was a
new kind of `Actor`? So our two new classes `Sheep` and `SheepDog` are
going to be new kinds of `Animal`.

First we need to change `Animal` so that it doesn't assume everything
is a sheep. Change your `Animal.__init__` method like so:

.. code-block:: python
   :emphasize-lines: 5,6

   class Animal(Actor):

       all = []

       def __init__(self, img):
	   super(Animal, self).__init__(img)      


So now when we create an Animal we must specify the image we
want to use.

Now add this code under your `Animal` class:

.. code-block:: python

   class Sheep(Animal):

       def __init__(self):
	   super().__init__('sheep.png')

   class SheepDog(Animal):

       def __init__(self):
	   super().__init__('dog.png')

Finally, instead of creating new animals, we want to create new Sheep
or SheepDogs, so change your code where you have `Animal()` repeatedly to
the following -- and see how we've used a loop to create lots of sheep:

.. code-block:: python

   # Make a flock of sheep
   for i in range(15):
       Sheep()

   SheepDog()

When you press *Run* you should see that you how have a sheep dog, although
it behaves just like a sheep, so let's fix that next.

An obedient sheep dog
---------------------

When you look at the `Sheep` and `SheepDog` classes you'll see that
there really is only one difference: the image used. We actually
want the sheep dog to behave differently:

* To follow our instructions
* To herd the sheep, or put another way: we want the sheep to move away from
  the dog.

We can do these things by *overriding* the default behaviour we've created for
animals. So...

* Animals wander about, but SheepDogs follow the mouse
* Animals flock together, but Sheep move away from SheepDogs

Add a new method called `move` to your class `SheepDog` with this code:

.. code-block:: python
   :emphasize-lines: 6,7

   class SheepDog(Animal):

       def __init__(self):
	   super().__init__('dog.png')

       def move(self):
	   self.x, self.y = pygame.mouse.get_pos()

You'll also need to add `import pygame` to the top of your file.

Test this and see what difference it makes.

Run away from the sheep dog
---------------------------

We can now *override* the `attraction_to` method so that she Sheep
flock towards each other but run away from the sheep dog. Add this
new method to your `Sheep` class:

.. code-block:: python
   :emphasize-lines: 6-13

   class Sheep(Animal):

       def __init__(self):
           super().__init__('sheep.png')

       def attraction_to(self, other):
           d = self.distance_to(other)
           if isinstance(other, Sheep):
               # Attraction until we get too close
               return 0.1 * -math.cos(d/40)
           elif isinstance(other, SheepDog):
               # Move away
               return -100/d+0.001

There's quite a bit going on there, let's step through it:

* We get the distance between ourselves and the other animal
* We check if the other thing is a `Sheep` with `isinstance`, this
  tests the class against our criteria (we're testing for `Sheep` first)
* If it is a sheep then as before we have our herding formula
* Then if not, we test for a `SheepDog`
* If it is a sheep dog then we have a negagive attraction (a repulsion)
  which gets stronger the smaller the distance it.

Give it a test and see how it works.

Coming up soon
--------------

Let's set some kind of objective so that the game has a purpose...

