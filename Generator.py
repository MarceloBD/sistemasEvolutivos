import numpy as np 
import random
from Base import Base, Item

N_ITEMS_SELLING = 100
MUTATION_RANGE = 5

class Generator():

	def __init__(self, dis):
		self.dis = dis 
		self.product = np.zeros(10)
		self.mutation_chance = 0.1
		self.items_sold = 0 
		self.parent_product = self.product
		self.child = 1
		return

	def sell(self, has_parent_content):
		if(self.is_child and (not has_parent_content or not self.items_sold)):
			self.mutation()
		self.items_sold = 0
		for item in range(N_ITEMS_SELLING):
			result = self.dis.buy(self.product)
			if(result):
				self.items_sold += 1

	def mutation(self):
		for i in range(MUTATION_RANGE):
			x = random.randint(1,100)
			if (x <= 100*self.mutation_chance):
				index = random.randint(0,9)
				self.product[index] = Base.negate_bit(self.product[index])

	def get_items_sold(self):
		return self.items_sold

	def print_product(self):
		print (self.product)

	def get_product(self):
		return self.product

	def crossover(self, mask):
		for bit_pos in range(len(mask)):
			if(mask[bit_pos] == 1):
				self.product[bit_pos] = self.parent_product[bit_pos]

	def set_parent(self, parent, child):
		self.parent_product = parent.get_product() 
		self.child = child

	def is_child(self):
		return self.child