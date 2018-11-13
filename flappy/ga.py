from simulation import Simulation
#from mlp import Mlp 
from vision import Vision


class Ga():

	def __init__(self, number_of_chromosomes):
		self.chrom = [Simulation() for i in range(number_of_chromosomes)]
		#self.mlp = Mlp()
		vis = Vision()	
		return

	def run():
		for chrom, mlp in (self.chrom, self.mlp):
			mlp.predict(vis.get_distance(), chrm.get_dist_to_center(vis))
 			
   '''
	def mutation():
		mlp.weight_mutation()

	def crossover():


	def selection():

	'''