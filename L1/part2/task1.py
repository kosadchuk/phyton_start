class Rectangle:

	def __init__(self, length=1, width=1):
		self.length = length
		self.width = width

	def set_length(self, length):
		if (length > 0) and (length < 20):
			self.length = length
			return True
		else:
			return False

	def get_length(self):
		return self.length

	def get_perimetr(self):
		return 2 * (self.length + self.width)

	def get_area(self):
		return self.length * self.width




rect = Rectangle(2, 4)
print('Perimetr', rect.get_perimetr())
print('Area', rect.get_area())