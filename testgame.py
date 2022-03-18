from random import randint


class character(object):
	def __init__(self):

	#can create variables with self and no input params. 
	# without self the code will still "execute" first call:  <bound method character.attack of <__main__.player object at 0x000001CD1BD9BC70>> this will be the message. String then ... object location?
		self.attack = randint(0,9)

	def attack(self, attack):
		pass
	
	def health(self, health):
		pass
	
	def level(self, level):
		pass

	def weapon(self):
		pass

	def armor(self):
		pass
	
	

class player(character):
	#def __init__(self):
	
		#self.phealth = phealth
		#self.pattack = pattack

	def playerattack(self):
		setattack = self.attack
	#does not solidify the number in "setattack", each outside call will change it.
		return setattack
		
	#need to return this call and not "print()" it. With the return you can store the int and hold it in an outside variable
		#return randint(0,9)
	
	
'''
#commenting out before implementation
class enemy(character):
	

class boss(character):
	#better to add or take from other classes or not use them.
	def __init__(self):
'''

testone = player()
#second call will change the randomizer
testtwo = player()

print(testone.playerattack())
print(testtwo.playerattack())

rannum = testone.playerattack()
print("first call: ",rannum)
print("second call: ",rannum)

