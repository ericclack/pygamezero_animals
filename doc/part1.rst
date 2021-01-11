.. _part1:

Part 1
======

In part 1 we're going to create our first new class to model a
single sheep, and then later a whole flock.

Getting Started
---------------

Create a new file in Mu and enter the following lines:

.. code:: python
	  
   WIDTH = 500
   HEIGHT = 400
   TITLE = "Animal Simulation"

Press **Run** and save the file as :code:`animals.py` in your :code:`mu_code` directory.

You should see a new, empty window appear.

Creating an animal
------------------

You remember that we use Actor objects to draw sprites on the screen?
If not, take a look at `Flappy Bird Tutorial`_ for a nice simple
introduction.

So we are going to create our own specialised version of an Actor to
represent our on-screen animals.

First, import the random library as we'll need this to position the
animals. Add the :code:`import random` line as the first line of your
code.

Now let's add our new class. Add this code:

.. code:: python

   class Animal(Actor):

       def __init__(self):
	   super().__init__('sheep.png')
	   self.x = random.randint(0, WIDTH)
	   self.y = random.randint(0, HEIGHT)


So what does all that mean? Well :code:`class Animals` creates a new
class called Animal. And an *Animal* is a specialised form of an *Actor*
because we said :code:`class Animal(Actor)`. That means that *Animal* can
do everything *Actor* can do, which is handy because it means it already
knows how to draw itself and move around the screen. 

The function (or more correctly, method) :code:`__init__` is called
the constructor, it's what we want to happen when we make a new
*Animal*.

So let's do that, let's make a new animal. Add this code under your
class and *don't indent it* as we want this to be *outside* the class
code.:

.. code:: python

   a = Animal()

And to draw it, add this:

.. code:: python

   def draw():
       a.draw()

Now *Run* your program to see what happens. 

So we have a white dot on the screen. This is supposed to represent a
sheep! We can make it look nicer later.

Let's add some movement
-----------------------

Functions inside classes are called *methods*. Functions outside are
just called functions. This is important to remember, as you'll see in
a minute.

So let's add a new *method* to *Animal* called *move* -- you will need
to ensure that this code is indented to match the :code:`__init__`
method:

.. code:: python

   def move(self):
	  self.x += 1
	  self.y += 0.5

When does this function get called, when does the code run?

Never! Let's fix that. Add a new *function* at the end of your program:
   
.. code:: python

   def update():
     a.move()

Now if you *Run* this code you'll see your white dot move, and make a line
across the screen.

More animals
------------

We can easily create more animals, by adding code like this:

.. code:: python

   b = Animal()

However, they won't get drawn or move because we don't reference *b* in our
*draw* or *update* functions. Let's fix that.

We could just add :code:`b.move()` but then if we wanted to add more
we'd have a lot of typing to do. So the way we keep track of many
items is to use a *list* and a nice way to do this with classes is to
get the class to keep the list for us.

Add this code between the class definition and the :code:`__init__` method::

  all = []

And this code as the last line of the :code:`__init__` method::

        Animal.all.append(self)
	
So your class looks like this:

.. code:: python

   class Animal(Actor):

       all = []

       def __init__(self):
	   super().__init__('sheep.png')
	   self.x = random.randint(0, WIDTH)
	   self.y = random.randint(0, HEIGHT)
	   Animal.all.append(self)

       def move(self):
	   self.x += 1
	   self.y += 0.5

Now each time we create an animal, it gets added to the *all* list.

Now change the functions *draw* and *update* like so:

.. code:: python

   def draw():
       for a in Animal.all: a.draw()

   def update():
       for a in Animal.all: a.move()

Finally, we have a simpler way to create an animal, we can just do this: ::

  Animal()
  Animal()
  Animal()

That creates 3 animals. Try it and run your code to see it working.

Moving in different directions
------------------------------

OK, the sheep are pretty boring, let's make them move randomly.

In the method *move* change the code so that it is random: ::

   def move(self):
     self.x += random.uniform(-1,1)
     self.y += random.uniform(-1,1)

And let's also clear the screen in draw so that we don't leave trails behind the sheep: ::

   def draw():
     screen.clear()
     for a in Animal.all: a.draw()

Hmmm... have you noticed that the sheep seem to wobble back and forth, and don't really go anywhere? Let's fix that by giving each sheep a x and y speed when we create them. We set up this kind of thing in the constructor method (in :code:`__init__`):

Add these two lines before the *append* statement: ::

   self.xspeed = random.uniform(-1,1)
   self.yspeed = random.uniform(-1,1)

Can you see what you need to change in the *move* method next to use
these two new variables?

So your class should now look like this: ::

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

Sheep flock together
--------------------

So our sheep are not very sheep like. They are not interested in each
other, they just head off in a straight line and eventually leave the
screen and never come back. Let's fix this in :ref:`part2`.
     
.. _`Flappy Bird Tutorial`: https://tinyurl.com/y37qxb5h
