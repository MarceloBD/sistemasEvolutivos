#from mlp import Mlp
from vision import Vision
import numpy as np 
from simulation import Simulation
from ga import Ga
from mlp import Mlp 

NUMBER_CHROMOSOMES = 50
EPOCHS = 50

if __name__ == '__main__':
#	mlp = Mlp()
#	train = np.array([[50., 50., 0.],
#			 			[25., 25., 1.],
#			 			[15., 25., 1.],
#Y			 			[30., 30., 0.],])

#	mlp.set_train(train[:,0:2], train[:,2])
#	mlp.train()
#	mlp.predict(np.array([[50.,50.]]))
	
	vision = Vision()
	print('start')
	vision.get_train_imgs()
	vision.get_all_parameters()
	#vision.get_bird('images/1.png')
	
	'''
	vision.get_borders('images/29.png')
	last_px, pxright = vision.find_borders_values()
	vision.get_pipe_pixel(last_px, pxright, 'images/processed/0.png')
	vision.get_center('images/processed/0.png')
	'''
	"""
	mlp = Mlp()
	mlp.load_mlp()
	vis = Vision()
	vis.play(mlp)
	"""

	'''

	ga = Ga(NUMBER_CHROMOSOMES)
	ga.set_train_set([
		# ['images/processed/46.png'],
		# ['images/processed/47.png'],
		# ['images/processed/48.png'],
		# ['images/processed/49.png'],
		# ['images/processed/50.png'],
		# ['images/processed/51.png'],
		# ['images/processed/52.png'],
		# ['images/processed/53.png'],
		# ['images/processed/54.png'],
		# ['images/processed/55.png'],
		['images/processed/56.png'],
		['images/processed/57.png'],
		['images/processed/58.png'],
		['images/processed/59.png'],
		['images/processed/60.png'],
		['images/processed/61.png'],
		['images/processed/62.png'],
		['images/processed/63.png'],
		['images/processed/64.png'],
		['images/processed/65.png'],
		['images/processed/66.png'],
		['images/processed/67.png'],
		['images/processed/68.png'],
		['images/processed/69.png'],
		['images/processed/70.png'],
		['images/processed/71.png'],
		['images/processed/72.png'],
		['images/processed/73.png'],
		['images/processed/74.png'],
		['images/processed/75.png'],
		['images/processed/76.png'],
		['images/processed/77.png'],
		['images/processed/78.png'],
		['images/processed/79.png']])
	ga.run(EPOCHS)
	'''
	'''
	sim = Simulation()
	sim.update()
	sim.jump()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.jump()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	sim.update()
	'''
