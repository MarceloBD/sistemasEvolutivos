from simulation import Simulation
from mlp import Mlp 
from vision import Vision
import cv2


class Ga():

	def __init__(self, number_of_chromosomes):
		self.chrom = [Simulation() for i in range(number_of_chromosomes)]
		self.mlp = [Mlp() for i in range(number_of_chromosomes)]
		self.vis = Vision()	
		self.train_set = []
		return

	def set_train_set(self, filenames):
		self.train_set = filenames

	def run(self, epochs):
		for epoch in range(epochs):
			for mlp in self.mlp:
				self.mutation(mlp)
			for chrom in self.chrom:
				chrom.reset()
			self.simulate(epoch)

	def simulate(self, epoch):
		for filename in self.train_set:
			filename = filename[0]
			img = cv2.imread(filename)
			cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			color = [0, 0, 0]
			i = 0 
			for chrom, mlp in zip (self.chrom, self.mlp):
				if(not chrom.is_alive):
					continue
				jump = mlp.predict([[self.vis.get_distance(filename), chrom.get_dist_to_center(self.vis.get_center(filename))]])	
				print('parameterssssss' ,self.vis.get_distance(filename), chrom.get_dist_to_center(self.vis.get_center(filename)))
				if(jump[0]):
					print('----------------------- jump ----------------------------')
					chrom.jump()
				if(chrom.is_alive()):
					img = self.draw_all_squares(chrom, img, color)
				color[0] += 5
				print("color", color)
				print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', i)
				chrom.print()
				chrom.update(self.vis.get_distance(filename))
				i += 1
			#print('here')
			#if(epoch == 30):
			cv2.imshow('teste', img)
			cv2.waitKey(0) 		

	def draw_all_squares(self, chrom, img, color):
 		return chrom.draw(img, color)

	
	def mutation(self, mlp):
		mlp.weight_mutation()

	'''
	def crossover():


	def selection():

	'''