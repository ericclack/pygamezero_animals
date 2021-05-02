.. _part3:

Part 3
======

So let's add a sheep dog so that we can try and herd the sheep
and explore forces of fear as well as attraction.

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


Add this code under your `Animal` class:

.. code-block:: python

   class Sheep(Animal):

       def __init__(self):
	   super().__init__('sheep.png')

   class SheepDog(Animal):

       def __init__(self):
	   super().__init__('dog.png')

Finally, instead of creating new animals, we want to create new Sheep
or SheepDogs, so change your code where you have `Animal()` repeatedly to
the following -- and see how we've used a loop to create lots of animals:

.. code-block:: python

   # Make a flock of sheep
   for i in range(15):
       Sheep()

   SheepDog()

When you press *Run* you should see that you how have a sheep dog, although
it behaves just like a sheep, so let's fix that now.

When you look at the `Sheep` and `SheepDog` classes you'll see that
there really is only one difference: the 
