class Bottle:
	""" run through of the class options without having to use self variables"""

	def __init__(self, volume, beverage):

		self.volume = volume
		self.beverage = beverage

	def pouring(self):

		print('pouring')
	
	def filling(self):
		
		print('filling')


class GlassBottle(Bottle):
	""" working with child classes to gain confidence is class items and the uses"""
	
	def pouring(self):

		print('pouring: ',self.beverage)


class Can:
	"""Displaying variables in other functions that are still within the same class, but not called on 		function params line"""

	def __init__(self, beverage):
		
		self.beverage = beverage

	def look(self):

		print(self.beverage,"Is in the can.")


class Jar:
	""" gaining confidence in how i can still use logics in functions in classes"""

	def __init__(self, content):
	
		self.content = content

	def contents(self):

		if self.content == 'jam':

			print("thats jam")

		else: 

			print("That's not jam")



class Var:
	"""test to see about not having self variables that will still display after runtime"""

	def __init__(self, num_one, num_two):

		self.num_one = num_one
		self.num_two = num_two
		pass

	def no_self(self):
		add = self.num_one + self.num_two

		sub = self.num_one - self.num_two

		print("add is: ", add)
		print("sub is: ", sub)


class One:
	"""Going to try and use two classes (One() and Two()), using Two() to call into One()"""

	def __init__(self):
		pass

	def function(self):
		print("This is the function within One()")


class Two:
	""" Using class One() as a pass, sans child param, to retrieve functions and use them"""

	def __init__(self):
		pass

	def funkt(self):

		base = One()
		base.function()
		print("This is the bottom of the function(funkt) within Two()")

class New:
	"""Want to try calling the function after the fact. On code execute. Same as classes One and Two 	but not assigning variables within the class and just calling functions. """

	def __init__(self, new_input):
		self.new_input = new_input

	def func_call(self):
		print("this is func_call within New()and this is the contents of new_input variable: ", new_input)

class other_New:
	"""New() partner the function call does not work directly, because it has no attribute called 		func_call"""

	def __init__(self):
		pass

	def other_func(self):
		
		other_New.other_func.func_call()
		print("end of other_func() within other_New() class")

'''
# this order does not work
other = other_New()

other(New("this thing"))
'''
'''
class Engine(object):
	""" Now to figure this out. This comes from learn python the hardway: lessson 43. This "Engine" is 	a part of the lessons game. This seems like the parent class. But it isnt set up that way. It is 	
	seperate. 
	"""

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

			current_scene.enter()

class Map(object):
	
	scenes = {
		'central_corridor': 'central corridor',
		'laster_weapon_armory': 'LaserWeaponArmory',
		'the_bridge': 'TheBridge',
		'escape_pod': 'EscapePod',
		'death': 'Death',
		'finished': 'Finished',
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')

a_game = Engine(a_map)

a_game.play()

# have to call the actual play function. Dingus.
'''

class Map:
	""" I want to see this break down of elements. So far the functions require params. Inserted print statement to next_scene. Print statement does not execute"""
	scenes = {
		'1' : One(),
		'2': 2,
		'3': 3,
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		print("this is next_scene",scene_name)
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)

class One:
""" Can't seem to replicate the execution that this code is from. Obviously I am missing some more bits of logic. But this is just strange. I know i am fighting the original programmers logic in this code. But i jsut want to know. """

	def printthis(self):
		print("HERE IS ONE")

thru = Map("start")

thru.next_scene('1')