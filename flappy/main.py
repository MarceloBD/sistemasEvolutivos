#from mlp import Mlp
from vision import Vision
import numpy as np 
from simulation import Simulation

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
	#vision.get_train_imgs()
	#vision.get_all_parameters()
	#vision.get_bird('images/1.png')
	#vision.get_borders('images/29.png')
	#last_px, pxright = vision.find_borders_values()
	#vision.get_pipe_pixel(last_px, pxright, 'images/0.png')
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