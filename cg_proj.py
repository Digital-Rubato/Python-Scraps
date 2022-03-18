class Enemy:
	
	def __init__(self, health, attack, defense):
	
		self.attack = attack
		self.defense = defense
		self.health = health		

	def give(self, attack):
		self.attack

	def take(self, defense, health):
		self.defense
		self.health

class Player(Enemy):

	def give(self, attack):
		
		return attack
	
	def take(self, defense, health):
		pass
