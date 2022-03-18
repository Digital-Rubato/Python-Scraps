class Enemy:
	""" base class. Player class will child off of this. Enemy will have an attack some defense and  will drop 'gold' for the player to use in the Shop() """

	def __init__(self, attack, defense):
		self.attack = attack
		self.defense = defense
		
	def health(self):
		pass
		hp = 10
		
	def attack(self):
		self.attack
		pass

	def defense(self):
		self.defense
		pass
	
	def drop(self):
		pass
	
		

class Player(Enemy):
	""" """
	"""
	#def attack(self, weapon):
		#self.weapon
		#self.attack
		#damage = self.weapon + self.attack
		#print(damage)
	"""
	def attack(weapon, attack):
		damage = weapon + attack
		print(damage)
	
	

'''
class Boss(Enemy):
	pass
	self.attack = 10
	self.defense = 10

def attack(weapon, attack):
	damage = weapon + attack
	print(damage)
'''
w1 = int(input("weapon: "))
a1 = int(input("attack: "))
test_this = Player(w1, a1)
test_this.attack()


