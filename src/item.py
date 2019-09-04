class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		print(f'name: {self.name}')
		print(f'description: {self.description}')