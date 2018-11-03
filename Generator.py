import numpy as np 
import random
from Base import Base, Item

class Generator():

	def __init__(self, dis):
		self.dis = dis 
		self.product = np.zeros(10)
		self.mutation_chance = 0.5
		self.items_sold = 0 
		return

	def sell(self):
		self.mutation()
		result = self.dis.buy(self.product)
		if(result):
			self.items_sold += 1
			return Item.SOLD
		else:
			return Item.NOT_SOLD

	def mutation(self):
		x = random.randint(1,100)
		if (x <= 100*self.mutation_chance):
			index = random.randint(0,9)
			self.product[index] = Base.negate_bit(self.product[index])

	def get_items_sold(self):
		return self.items_sold

	def print_product(self):
		print (self.product)

	def crossover(self, mask):
		for bit_pos in range(len(mask)):
			if(mask[bit_pos] == 0):
				self.product[bit_pos] = Base.negate_bit(self.product[bit_pos])
