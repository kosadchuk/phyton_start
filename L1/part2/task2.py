import math

class Rational:
	def __init__(self, a=1, b=1):
		self.a = a // math.gcd(a, b)
		self.b = b // math.gcd(a, b)

	def rational_division(self):
		return str(self.a) + "/" + str(self.b)


	def rational_floating_point_division(self):
		return f"{self.a / self.b:.3}"