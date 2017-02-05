# base class
class Item():

	def __init__(self, name, description):
		self.name = name
		self.description = description
		
	def __str__(self):
		return "{}:\n{}\n".format(self.name, self.description)
		
	def get_name(self):
		return self.name

	def getDescription(self):
		return self.description


class Gold(Item):

	def __init__(self, amount):
		self.amount = amount
		super().__init__("Gold", "A currency used in the time of the king.")

	def returnAmount(self):
		return self.amount

class Weapon(Item):

	def __init__(self, name, description, damage, speedModifier):
		self.damage = damage
		self.speedModifier = speedModifier
		super().__init__(name, description)

	def damageOutput(self):
		return self.damage

	def getSpeedModifier(self):
		return self.speedModifier

class Armor(Item):
	def __init__(self, name, description, defensiveModifier, speedModifier):
		self.defensiveModifier = defensiveModifier
		self.speedModifier = speedModifier
		super().__init__(name, description)

		def getDefensiveModifier(self):
			return self.defensiveModifier

		def getSpeedModifier(self):
			return self.speedModifier

class HealingItem(Item):
	def __init__(self, name, description, healingAmt):
		self.healingAmt = healingAmt
		super().__init__(name, description)

	def getHealingAmount(self):
		return self.healingAmt

##base class
#class Weapon(Item):

#	def __init__(self, name, description, value, damage, speed):
#		self.speed = speed
#		super().__init__(name, description, damage, value)
		
#	def __str__(self):
#		return "{}\n=====\n{}\nValue: {}\nDamage: {}\nSpeed: {}\n".format(self.name, self.description, self.value, self.effect, self.speed)
##base class	
#class Armor(Item):

#	def __init__(self, name, description, protection, value, speed):
#		self.speed = speed
#		super().__init__(name, description, protection, value)
##real item class	
#class Gold(Item):

#	def __init__(self, amt):
#		self.amt = amt
#		super().__init__('Gold', 'A round, golden coin.', None, 1)
##real item class
#class Potion(Item):

#	def __init__(self, heal):
#		self.heal = heal
#		super().__init__('Potion', 'A ruby red potion in a crystal flask. Restores health.', 10, 100)
##real item class				
#class Broadsword(Weapon):

#	def __init__(self):
#		super().__init__("Broadsword", "A double edged blade fit for wide slashes.", 100, 10, 5)
##real item class		
#class Elvish_Sword(Weapon):

#	def __init__(self):
#		super().__init__("Elvish Sword", "A graceful, eloquent blade of great antiquity.", 200, 8, 10)
##real item class		
#class Rugged_Gtswrd(Weapon):

#	def __init__(self):
#		super().__init__("Rugged Greatsword", "A weathered bronze greatsword with a unique quality.", 50, 20, 2)
##real item class
#class Leather_Armor(Armor):

#	def __init__(self):
#		super().__init__("Leather Armor", "Light armor. Allows for maximum mobility.", 5, 50, 10)
##real item class		
#class Medium_Armor(Armor):

#	def __init__(self):
#		super().__init__("Half Plate Armor", "Medium armor. Provides a practical balance of defense and speed.", 10, 150, 5)
##real item class		
#class Heavy_Armor(Armor):

#	def __init__(self):
#		super().__init__("Plate Armor", "Heavy armor. Ensures a sturdy defense at the cost of encumbered movement.", 15, 500, 2)
		
