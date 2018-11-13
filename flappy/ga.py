from simulation import Simulation
from mlp import Mlp 
from vision import Vision


class Ga():

	def __init__(self, number_of_chromosomes):
		self.chrom = [Simulation() for i in range(number_of_chromosomes)]
		self.mlp = [Mlp() for i in range(number_of_chromosomes)]
		self.vis = Vision()	
		self.train_set = []
		return

	def set_train_set(self, filenames):
		self.train_set = filenames

	def run(self):
		for filename in self.train_set:
			for chrom, mlp in zip (self.chrom, self.mlp):
				mlp.predict([[self.vis.get_distance(filename), chrom.get_dist_to_center(self.vis.get_center(filename))]])
 			
	'''
	def mutation():
		mlp.weight_mutation()

	def crossover():


	def selection():

	'''