from items import *

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
		#self.items = []
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
	
	def get_name(self):
		return self.name
		
	def get_description(self):
		return self.description

	def printItems(self):
		for items in self.dict_of_items().keys():
			print("There is a " + self.dict_of_items()[items].get_name() + " here.")
		
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