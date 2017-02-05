from map import *
from room import *
from items import *

class Player():
	def __init__(self, room, _map):
		self.hp = 10
		# inventory is a list of Items
		# self.inventory = []
		self.inventory = {}
		self.speed = 10
		self.armor = 10
		self.current_room = room
		self.location = [0,0,0]
		self.map = _map
	
	def __str__(self):
		return "{}".format(self.current_room.get_coordinates())
		
	#def attack(self, _map):
		
	# coordinate system: [x, y, z]
	def move(self, direction):
		directions = {'n':[1,1],'north':[1,1],'s':[1,-1],'south':[1,-1],'e':[0,-1],'east':[0,-1],'w':[0,1],'west':[0,1],'up':[2,1],'u':[2,1],'down':[2,-1],'d':[2,-1]}
		
		self.location[directions[direction][0]] += directions[direction][1]
		for r in self.map.neighbours(self.current_room):
			if r.get_coordinates() == str(self.location):
				self.current_room = r
				if not self.current_room.visited:
					self.printLocation('')
					self.current_room.visited = True
				else:
					print(self.current_room.get_name())
					self.current_room.printItems()
				return
		self.location[directions[direction][0]] -= directions[direction][1]
		print(r.print_error(direction))

	def printLocation(self, inputStr):
		print(self.current_room)
		self.current_room.printItems()

	def print_inventory(self, inputStr):
		if len(self.inventory.keys()) == 0:
			print("You aren't carrying anything.")
		for itemName in self.inventory.keys():
			print(self.inventory[itemName])

	def add_to_inven(self, item):
		self.inventory[item.get_name().lower()] = item

	def pick_up(self, itemName):
		if len(itemName.split(' ')) > 1 and itemName.split(' ')[0] == 'take':
			itemName = itemName[5:]
		if itemName == 'all':
			self.pick_up_all()
		elif itemName in self.current_room.dict_of_items().keys():
			self.current_room.retrieve_item(itemName, self)
		else:
			print('There is no \"' + itemName + '\" here.')

	def pick_up_all(self):
		for itemName in list(self.current_room.dict_of_items().keys()):
			self.pick_up(itemName)

	def drop(self, itemName):
		if len(itemName.split(' ')) > 1 and itemName.split(' ')[0] == 'drop':
			itemName = itemName[5:]
		if itemName == 'all':
			self.dropAll()
		elif itemName in self.inventory.keys():
			self.current_room.add_item(self.inventory[itemName])
			del self.inventory[itemName]
			print('Dropped ' + itemName + '.')
		else:
			print('You aren\'t carrying a \"' + itemName + '\".')

	def dropAll(self):
		for itemName in list(self.inventory.keys()):
			self.drop(itemName)

	def doNothing(inputStr):
		print('')
