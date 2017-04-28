class Creature():
	"""description of class"""
	def __init__(self, health, speed, name, description, damage):
		self.hp = health
		self.name = name
		self.spd = speed
		self.desc = description
		self.attackPower = damage
		self.alive = True
		self.deathMessage = "The " + self.name + " falls to the ground, dead."
	
	def TakeDamage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			self.alive = False
			print(self.deathMessage)

	def GetAttackPower(self):
		return self.attackPower

	def IsAlive(self):
		return self.alive

	def GetDescription(self):
		return self.desc
	
	def GetSpeed(self):
		return self.spd

	def GetName(self):
		return self.name

	def SetDeathMessage(self, message):
		self.deathMessage = message

#Real creature
class Troll(Creature):
	
	def __init__(self):
		super().__init__(20, 5, "Troll", "A huge, menacing troll stands before you, axe brandished.", 4)
		
	def TakeDamage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			self.alive = False
			print("The troll crumples to the ground, it's eyes blank. It slowly dissolves into black smoke, along with it's weapon.")

