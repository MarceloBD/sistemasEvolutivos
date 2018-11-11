from Generator import Generator
from Discriminator import Discriminator
import numpy as np 
import copy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

NUMBER_OF_GENES = 100
EPOCHS = 200


def selection(gen):
	items_sold = [gen[gene].get_items_sold() for gene in range(NUMBER_OF_GENES)]
	biggest_index = np.argsort(-np.array(items_sold))[:5]
	biggest_gen = [gen[index] for index in biggest_index]
	for gene in range(NUMBER_OF_GENES):
		gen[gene].set_parent(biggest_gen[int(gene/20)], int(not is_parent(gen[gene], biggest_gen)))
	#[gen[i].print_product() for i in range(len(gen))]
	[biggest_gen[i].print_product() for i in range(len(biggest_gen))]
	return gen, biggest_gen

def is_parent(gen, parent_list):
	parent = 0
	for big in parent_list:
			if(gen == big):	
				parent = 1
	return parent

def has_parent_content(gen, parent_list):
	has_parent_content = 0
	for big in parent_list:
			if(np.array_equal(gen.get_product(), big.get_product())):	
				has_parent_content = 1
	return has_parent_content	

def crossover(gen, biggest_gen):
	mask = np.random.randint(8, size=10)
	for i in range(NUMBER_OF_GENES):
		if (is_parent(gen[i], biggest_gen) == 0):
			gen[i].crossover(mask)
	return gen 		

def run(gen, biggest_gen):
	for gene in range(NUMBER_OF_GENES):
		gen[gene].sell(has_parent_content(gen[gene], biggest_gen))

	[print(gen[gene].get_items_sold()) for gene in range(NUMBER_OF_GENES)]
	[market_history.append(gen[gene].get_items_sold()) for gene in range(NUMBER_OF_GENES)] 


def plot_genes_market(gen):
	colors = cm.rainbow(np.linspace(0, 1, NUMBER_OF_GENES))
	for gene, c in zip(np.arange(NUMBER_OF_GENES), colors):
		plt.plot( np.arange(EPOCHS), [market_history[gene+i*NUMBER_OF_GENES] for i in range(EPOCHS)])
	plt.show()	

if __name__ == '__main__':
	gen = []
	dis = Discriminator()
	market_history = []

	for gene in range(NUMBER_OF_GENES):
		gen.append(Generator(dis))
	run(gen, [])

	running = 1
	for i in range(EPOCHS):
		gen, biggest_gen = selection(gen)
		gen = crossover(gen, biggest_gen)	
		run(gen, biggest_gen)

	plot_genes_market(gen)