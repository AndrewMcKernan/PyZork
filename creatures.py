class Creature():
	"""description of class"""
	def __init__(self, health, speed, name, description, damage):
		self.hp = health
		self.name = name
		self.spd = speed
		self.desc = description
		self.dmg = damage
		self.alive = True
	
	def TakeDamage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			self.alive = False

#Real creature
class Troll(Creature):
	
	def __init__():
		super().__init__(self, 20, 5, "Troll", "A huge, menacing troll stands before you, axe brandished.", 4)
		
	def TakeDamage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			self.alive = False
			print("The troll crumples to the ground, it's eyes blank. It slowly dissolves into black smoke, along with it's weapon.")
