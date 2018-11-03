import numpy as np
import random
import copy

class Discriminator():
	def __init__(self):
		self.true_data = np.empty((0,10), int)
		self.true_data = np.append(self.true_data, [np.ones(10)], axis=0)
		return

	def buy(self, product):
		for data in self.true_data:
			pseudo_data = self.data_noise(data) 
			if(np.array_equal(product, pseudo_data)):
				return 1
		return 0

	def data_noise(self, data):
		data_with_noise = copy.copy(data)
		for bit in range(random.randint(0,5)):
			x = random.randint(0,10)
			if (x < 10):
				index = random.randint(0,9)
				data_with_noise[index] = ~int(data_with_noise[index]) + 2 
		return data_with_noise
