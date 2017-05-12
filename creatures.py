class Creature():
	"""description of class"""
	def __init__(self, health, speed, name, damage):
		self.maxHP = health
		self.hp = health
		self.name = name
		self.spd = speed
		self.attackPower = damage
		self.alive = True
		self.deathMessage = "The " + self.name + " falls to the ground, dead."
		self.fullHealthMessage = ""
		self.halfHealthMessage = ""
		self.quarterHealthMessage = ""

	def __str__(self):
		if self.hp <= self.maxHP / 4:
			return "{}\n".format(self.quarterHealthMessage)
		elif self.hp <= self.maxHP / 2:
			return "{}\n".format(self.halfHealthMessage)
		else:
			return "{}\n".format(self.fullHealthMessage)

	
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

	def SetFullHealthMessage(self, message):
		self.fullHealthMessage = message

	def SetHalfHealthMessage(self, message):
		self.halfHealthMessage = message

	def SetQuarterHealthMessage(self, message):
		self.quarterHealthMessage = message

	def GetDeathMessage(self):
		return self.deathMessage

	def TakeDamage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			self.alive = False
			print(self.GetDeathMessage())

#Real creature
class Troll(Creature):
	
	def __init__(self):
		super().__init__(20, 5, "Troll", 4)
		self.SetDeathMessage("The troll crumples to the ground, its eyes blank. It slowly dissolves into black smoke, along with its weapon.")
		self.SetFullHealthMessage("A huge, menacing troll stands before you, brandishing its bloody greataxe.")
		self.SetHalfHealthMessage("The troll glares at you angrily, rage burning in its eyes.")
		self.SetQuarterHealthMessage("The troll leans on the hilt of its axe, barely holding onto life.")
		
	

