from simulation import Simulation
from mlp import Mlp 
from vision import Vision
import cv2
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.cm as cm


SELECTION_RANGE = 5


class Ga():

	def __init__(self, number_of_chromosomes):
		self.chrom = [Simulation() for i in range(number_of_chromosomes)]
		self.mlp = [Mlp() for i in range(number_of_chromosomes)]
		self.vis = Vision()	
		self.train_set = []
		self.number_of_chromosomes = number_of_chromosomes
		self.number_of_chrom_per_group = self.number_of_chromosomes/SELECTION_RANGE
		return

	def set_train_set(self, filenames):
		self.train_set = filenames

	def run(self, epochs):
		self.epochs = epochs
		for epoch in range(epochs):
			for chrom, mlp in zip(self.chrom, self.mlp):
				if(not chrom.is_parent(mlp)):
					self.mutation(mlp)
			for chrom in self.chrom:
				chrom.reset()
			self.simulate(epoch)
			self.selection(epoch)
			self.crossover()
		self.save_best()
		self.plot_fit_graph()


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
				#print('parameterssssss' ,self.vis.get_distance(filename), chrom.get_dist_to_center(self.vis.get_center(filename)))
				if(jump[0]):
					#print('----------------------- jump ----------------------------')
					chrom.jump()
				if(chrom.is_alive()):
					img = self.draw_all_squares(chrom, img, color)
				color[0] += 5
				#print("color", color)
				#print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', i)
				#chrom.print()
				chrom.update(self.vis.get_distance(filename))
				i += 1
		#	cv2.imshow('teste', img)
		#	cv2.waitKey(0)
		#	print('img') 	
		#	if(epoch >20):
		#		cv2.imshow('teste', img)
		#		cv2.waitKey(0)
		#		print('img') 		
		for chrom in self.chrom:
			chrom.save_fit_in_history()
			#print('here')
			

	def draw_all_squares(self, chrom, img, color):
 		return chrom.draw(img, color)

	
	def mutation(self, mlp):
		mlp.weight_mutation()

	def crossover(self):
		#mask = np.random.randint(8, size=10)
		for i in range(self.number_of_chromosomes):
				self.chrom[i].crossover(self.mlp[i])
		return 

	def selection(self, epoch):
		fits = [chrom.get_fit() for chrom in self.chrom]
		biggest_fits_i = np.argsort(-np.array(fits))[:SELECTION_RANGE]
		biggest_fits_mlp = [self.mlp[i] for i in biggest_fits_i]
		biggest_fits_chrom = [self.chrom[i] for i in biggest_fits_i]
		#print('melhores fittttttttttttttttsssssssssss ----')
		#[print(chrom.get_fit_of_epoch(epoch)) for chrom in biggest_fits_chrom]
		passed_parent = 0
		for chrom_i in range(self.number_of_chromosomes):
			if(not self.is_parent(self.mlp[chrom_i], biggest_fits_mlp)):
				self.chrom[chrom_i].set_parent(biggest_fits_mlp[int((chrom_i-passed_parent)/self.number_of_chrom_per_group)])
			else:
				passed_parent += 1

		for chrom, mlp in zip(biggest_fits_chrom, biggest_fits_mlp):
			chrom.set_parent(mlp)

	def is_parent(self, mlp, biggest_fits_mlp):
		parent = False
		for c in biggest_fits_mlp:
			if(mlp == c):
				parent = True
		return parent

	def plot_fit_graph(self):
		colors = cm.rainbow(np.linspace(0, 1, self.number_of_chromosomes))
		for chrom, c in zip(np.arange(self.number_of_chromosomes), colors):
			plt.plot( np.arange(self.epochs), [self.chrom[chrom].get_fit_of_epoch(i) for i in range(self.epochs)])
		plt.show()

	def save_best(self):
		fits = [chrom.get_fit() for chrom in self.chrom]
		biggest_fits_i = np.argsort(-np.array(fits))[:1]
		biggest_fits_mlp = [self.mlp[i] for i in biggest_fits_i]
		biggest_fits_mlp[0].save_mlp()
