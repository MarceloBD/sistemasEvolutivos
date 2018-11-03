import numpy as np 
import random

class Generator():

	def __init__(self, dis):
		self.dis = dis 
		self.product = np.zeros(10)
		self.mutation_chance = 0.5
		return

	def sell(self):
		self.mutation()
		result = self.dis.buy(self.product)
		if(result):
			print('sold')
			return 1
		else:
			print('not sold')
			return 0

	def mutation(self):
		x = random.randint(1,100)
		if (x <= 100*self.mutation_chance):
			index = random.randint(0,9)
			self.product[index] = ~int(self.product[index]) + 2
