from Generator import Generator
from Discriminator import Discriminator
import numpy as np 
import copy


NUMBER_OF_GENES = 50

def selection(gen):
	items_sold = [gen[gene].get_items_sold() for gene in range(NUMBER_OF_GENES)]
	biggest_index = np.argsort(-np.array(items_sold))[:5]
	biggest_gen = [gen[index] for index in biggest_index]
	new_gen = copy.deepcopy(gen)
	for gene in range(NUMBER_OF_GENES):
		new_gen[gene] = copy.deepcopy(biggest_gen[int(gene/10)])
	return new_gen

def crossover(gen):
	for i in range(NUMBER_OF_GENES):
		gen[i].crossover([0,1,1,0,1,1,1,1,1,0])
	return gen 		

def run(gen):
	for epoch in range(NUMBER_OF_GENES):
		for i in range(NUMBER_OF_GENES):
			gen[i].sell()

if __name__ == '__main__':
	gen = []
	dis = Discriminator()
	for gene in range(NUMBER_OF_GENES):
		gen.append(Generator(dis))
	
	run(gen)

	[print(gen[i].get_items_sold()) for i in range(NUMBER_OF_GENES)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_items_sold()) for i in range(NUMBER_OF_GENES)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_items_sold()) for i in range(NUMBER_OF_GENES)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_items_sold()) for i in range(NUMBER_OF_GENES)]

	new_gen = selection(gen)
	gen = crossover(new_gen)

	run(gen)

	[print(gen[i].get_items_sold(), gen[i].print_product()) for i in range(NUMBER_OF_GENES)]