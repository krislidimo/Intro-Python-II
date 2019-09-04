from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Welcome message
print('\n_-************* Welcome to ~The Game~ *************-_\n')
print('The best one! Way better than the other guys...\n')

print('Here\'s how to play:\n')
print('North  :n')
print('South  :s')
print('East   :e')
print('West   :w\n')
print('Quit   :q\n')

current_room = room['outside']

while True:

	# Printing Location & description
	print('-------------------------------------------------------')
	print(f'Location: {current_room.name}\n')
	print(f'Description: {current_room.description}\n')

	# Printing user options
	print(f'Options:')
	current_room.n_to and print(f'North [n]: {current_room.n_to.name}')
	current_room.s_to and print(f'South [s]: {current_room.s_to.name}')
	current_room.e_to and print(f'East  [e]: {current_room.e_to.name}')
	current_room.w_to and print(f'West  [w]: {current_room.w_to.name}')
	print(f'Quit  [q]')

	print(f'Items:')
	for item in current_room.items:
		print(f'Name: {item.name} Description: {item.description}')


	# Colecting user input
	direction = input('\nWhere would you like to go?: ').lower()

	# Conditional statments
	if direction == 'q':
		print('Thanks for playing!')
		break
	elif current_room.n_to and (direction == 'n'):
		current_room = current_room.n_to
	elif current_room.s_to and (direction == 's'):
		current_room = current_room.s_to
	elif current_room.e_to and (direction == 'e'):
		current_room = current_room.e_to
	elif current_room.w_to and (direction == 'w'):
		current_room = current_room.w_to
	else:
		print('\nNot a valid option buddy. [-_-]\n')
		continue

	# Winning condition
	# INCOMPLETE Currently does nothing.
	if current_room.name == 'WIN':
		print('\n*************Congratulations*************\n')
		print('*****************You win*****************')
		break