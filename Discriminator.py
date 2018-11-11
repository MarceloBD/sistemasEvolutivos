import numpy as np
import random
import copy
from Base import Base


NOISE_CHANCE = 0.1
NOISE_RANGE = 0.5

class Discriminator():
	def __init__(self):
		self.base = Base()
		self.true_parameters = self.base.give_parameters()
		return

	def buy(self, product):
		for parameters in self.true_parameters:
			pseudo_parameters = self.add_parameters_noise(parameters) 
			if(np.array_equal(product, pseudo_parameters)):
				return 1
		return 0

	def add_parameters_noise(self, parameters):
		parameters_with_noise = copy.copy(parameters)
		for bit in range(random.randint(0, int(NOISE_RANGE*len(parameters)))):
			x = random.randint(0,100)
			if (x < 100*NOISE_CHANCE):
				index = random.randint(0,9)
				parameters_with_noise[index] = Base.negate_bit(parameters_with_noise[index]) 
		return parameters_with_noise
