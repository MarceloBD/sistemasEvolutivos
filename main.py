from Generator import Generator
from Discriminator import Discriminator
import numpy as np 
import copy

def selection(gen):
	values = [gen[i].hit for i in range(50)]
	max_index = np.argsort(-np.array(values))[:5]
	max_gen = [gen[i] for i in max_index]
	new_gen = copy.deepcopy(gen)
	for i in range(50):
		new_gen[i] = copy.deepcopy(max_gen[int(i/10)])
	return new_gen

def crossover(gen):
	for i in range(50):
		gen[i].crossover([0,1,1,0,1,1,1,1,1,0])
	return gen 		

def run(gen):
	for epoch in range(50):
		for i in range(50):
			gen[i].sell()

if __name__ == '__main__':
	gen = []
	dis = Discriminator()
	
	for i in range(50):
		gen.append(Generator(dis))
	
	run(gen)

	[print(gen[i].get_hit()) for i in range(50)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_hit()) for i in range(50)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_hit()) for i in range(50)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_hit()) for i in range(50)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_hit(), gen[i].print_product()) for i in range(50)]