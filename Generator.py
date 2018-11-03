import numpy as np 
import random

class Generator():

	def __init__(self, dis):
		self.dis = dis 
		self.product = np.zeros(10)
		self.mutation_chance = 0.5
		self.hit = 0 
		return

	def sell(self):
		self.mutation()
		result = self.dis.buy(self.product)
		if(result):
			#print('sold')
			self.hit += 1
			return 1
		else:
			#print('not sold')
			return 0

	def mutation(self):
		x = random.randint(1,100)
		if (x <= 100*self.mutation_chance):
			index = random.randint(0,9)
			self.product[index] = ~int(self.product[index]) + 2

	def get_hit(self):
		return self.hit

	def print_product(self):
		print (self.product)

	def crossover(self, mask):
		for i in range(len(mask)):
			if(mask[i] == 0):
				self.product[i] = ~int(self.product[i]) + 2