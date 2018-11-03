from enum import Enum
import numpy as np 

class Item(Enum):
	SOLD = 1
	NOT_SOLD = 0

class Base():
	def __init__(self):
		self.true_parameters = np.empty((0,10), int)
		self.true_parameters = np.append(self.true_parameters, [np.ones(10)], axis=0)
		return

	@staticmethod
	def negate_bit(bit):
		return ~int(bit) + 2


	def give_parameters(self):
		return self.true_parameters