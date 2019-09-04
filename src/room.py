# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
	def __init__(self, name='', description=''):
		self.name = name
		self.description = description
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		self.items = []

	def __str__(self):
		return f'\n-------------------------------------------\n'  \
			f'name: {self.name}\n' \
			f'description: {self.description}\n' \
			f'n_to: {self.n_to and self.n_to.name}\n' \
			f's_to: {self.s_to and self.s_to.name}\n' \
			f'e_to: {self.e_to and self.e_to.name}\n' \
			f'w_to: {self.w_to and self.w_to.name}\n' \
			f'items: {self.items}\n' \
			f'-------------------------------------------\n'

	def addItem(self, item):
		self.items.append(item)