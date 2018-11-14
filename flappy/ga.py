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

	def run(self):
		for filename in self.train_set:
			filename = filename[0]
			img = cv2.imread(filename)
			cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
			color = [255, 0, 0]
			for chrom, mlp in zip (self.chrom, self.mlp):
				jump = mlp.predict([[self.vis.get_distance(filename), chrom.get_dist_to_center(self.vis.get_center(filename))]])	
				if(jump):
					chrom.jump()
				img = self.draw_all_squares(chrom, img, color)
				color[0] -= 1
				chrom.update()
			print('here')
			cv2.imshow('teste', img)
			cv2.waitKey(0) 			

	def draw_all_squares(self, chrom, img, color):
 		return chrom.draw(img, color)

	'''
	def mutation():
		mlp.weight_mutation()

	def crossover():


	def selection():

	'''