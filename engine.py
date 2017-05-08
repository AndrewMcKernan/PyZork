from items import *
from player import *
from room import *
from map import *


# game loop
def game(player, world):
	player.printLocation('')
	while True:
		userInput = input().rstrip().lstrip()
		action = userInput.lower()

		movementCommands = {'n':player.move, 'north':player.move, 's':player.move, 'south':player.move,
				   'w':player.move,'west':player.move,'e':player.move,'east':player.move,'u':player.move,
				   'up':player.move, 'd':player.move, 'down':player.move}

		verbNounCommands = {'l':player.printLocation, 'location':player.printLocation, 'i':player.print_inventory, 'inventory':player.print_inventory, 
				   'take':player.pick_up, 'drop':player.drop,'':player.doNothing, 'attack':player.Attack}
		# movement
		if action.split(' ')[0] in verbNounCommands:
			verbNounCommands[action.split(' ')[0]](action)
		elif action in movementCommands:
			movementCommands[action](action)
		else:
			print('I don\'t understand what \"' + userInput + '\" means.')
		player.GetCurrentRoom().Events(player)
