# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self, name, current_room):
		self.name = name
		self.current_room = current_room
		self.items = []

	def __str__(self):
		print(f'name: {self.name}')
		print(f'current_room: {self.current_room}')

	def pickUpItem(item):
		self.items.append(item)