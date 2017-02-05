from room import *
from map import *
from player import *
from items import *
from engine import *


world = Map('World')
start = Room('Starting Area', [0,0,0], 'A field.')
start.visited = True
start.add_item(Weapon("Broadsword", "A simple blade fit for wide slashes.", 1, 1))
start.add_item(Weapon("Elvish Blade", "A simple blade fit for wide slashes.", 1, 1))
barn = Room('Old Barn', [1,0,0], 'A rickety old barn.')
world.add_room(start)
world.add_room(barn)
world.add_path(start, barn)
world.add_path(barn, start)
char = Player(start, world)



game(char, world);
