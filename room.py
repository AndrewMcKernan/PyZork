from items import *
#from engine import Combat

class Room():
	
	def __init__(self, name, coordinates, description):
		if type(coordinates) is not list:
			ValueError("Coordinates must be a list [x,y,z]")
		if type(name) is not str:
			ValueError("Room name must be a string")
		if type(description) is not str:
			ValueError("Room description must be a string")
		self.name = name
		self.description = description
		self.coordinates = coordinates # [x,y,z]
		# items is a dictionary of Items
		self.items = {}
		self.errors = []
		self.enemies = []
		self.visited = False
	
	def __str__(self):
		return "{}\n{}\n".format(self.name, self.description)
		
	def rename(self, name):
		if type(name) is not str:
			ValueError("Room name must be a string")
		self.name = name
	
	def set_error(self, direction, error_msg):
		self.errors[direction] = error_msg
	
	def print_error(self, direction):
		if len(self.errors) < 4:
			return "You can't go that way."
		else:
			return "{}".format(self.errors[direction])
	
	def printEnemyBlockPath(self):
		enemyString = ""
		for enemy in self.enemies:
			enemyString += enemy.GetName() + ", "
		print("A " + enemyString[:-2] + " blocks your path.")


	def get_name(self):
		return self.name
		
	def get_description(self):
		return self.description

	def printItems(self):
		for items in self.dict_of_items().keys():
			print("There is a " + self.dict_of_items()[items].get_name() + " here.")

	def printRoom(self):
		print(self.get_name)
		printItems(self)
		
	def set_coordinates(self, coordinates):
		if type(coordinates) is not list:
			ValueError("Coordinates must be a list [x,y,z]")
		self.coordinates = coordinates
	
	def get_coordinates(self):
		return "{}".format(self.coordinates)
		
	def add_item(self, item):
		if type(item) is not Item:
			ValueError("Object is not an item")
		#print('Dropped', item.get_name(), '.')
		self.items[item.get_name().lower()] = item

	def addEnemy(self, enemy):
		self.enemies.append(enemy)
		
	def retrieve_item(self, itemName, player):
		for item in self.dict_of_items().values():
			if item.get_name().lower() == itemName:
				player.add_to_inven(item)
				print('Added ' + item.get_name() + ' to inventory.')
				del self.items[itemName]
				return
		print("There is no " + itemName + " here.")
		
	def dict_of_items(self):
		return self.items

	def getListOfEnemies(self):
		return self.enemies

	def printEnemies(self):
		for enemy in self.enemies:
			print(enemy)

	def Combat(self, player, enemy):
		if (player.GetSpeed() >= enemy.GetSpeed() and player.IsAttacking()):
			print("You attack, dealing " + str(player.DealDamage()) + " damage.")
			enemy.TakeDamage(player.DealDamage())
			if (enemy.IsAlive()):
				print("You are hit, taking " + str(enemy.GetAttackPower()) + " damage.")
				player.TakeDamage(enemy.GetAttackPower())
		else:
			print("You are hit, taking " + str(enemy.GetAttackPower()) + " damage.")
			player.TakeDamage(enemy.GetAttackPower())
			if (player.IsAlive() and player.IsAttacking()):
				print("You attack, dealing " + str(player.DealDamage()) + " damage.")
				enemy.TakeDamage(self.attackPower)
				
		player.SetAttacking(False)

	def Events(self, player):
		for enemy in self.enemies:
			self.Combat(player, enemy)
			if not enemy.IsAlive():
				self.enemies.remove(enemy)