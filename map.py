from room import Room
class Map:
	'''Graph class modified slightly for my game '''

	def __init__ (self, name):
		if type(name) is not str:
			ValueError("Map name must be a string")
		self._alist = {}
		self.name = name

	def rename (self, name):
		self.name = str(name)
		
	def get_name(self):
		return self.name
	
	def add_room (self, room):
		if type(room) is not Room:
			ValueError("Room is not 'Room' class")
		if room not in self._alist:
			self._alist[room] = set()

	def add_path (self, source, destination):
		if type(source) or type(destination) is not Room:
			ValueError("Source/dest is not 'Room' class")
		self.add_room(source)
		self.add_room(destination)
		self._alist[source].add(destination)

	def is_room (self, room):
		return str(room.get_coordinates()) in self._alist

	def neighbours (self, room):
		return self._alist[room]

	def rooms (self):
		return self._alist.keys()





