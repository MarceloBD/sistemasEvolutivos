from Generator import Generator
from Discriminator import Discriminator
import numpy as np 
import copy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

NUMBER_OF_GENES = 100
EPOCHS = 200
SELECTION_RANGE = 5
SAME_PARENT_GROUP = NUMBER_OF_GENES/SELECTION_RANGE

def selection(gens):
	items_sold = [gene.get_items_sold() for gene in gens]
	biggest_indices = np.argsort(-np.array(items_sold))[:SELECTION_RANGE]
	biggest_gens = [gens[index] for index in biggest_indices]
	for gene in range(NUMBER_OF_GENES):
		gens[gene].set_parent(biggest_gens[int(gene/SAME_PARENT_GROUP)], int(not is_parent(gens[gene], biggest_gens)))
	[biggest_gens[i].print_product() for i in range(len(biggest_gens))]
	return gens, biggest_gens

def is_parent(gen, parent_list):
	parent = 0
	for par in parent_list:
			if(gen == par):	
				parent = 1
	return parent

def has_parent_content(gen, parent_list):
	has_parent_content = 0
	for par in parent_list:
			if(np.array_equal(gen.get_product(), par.get_product())):	
				has_parent_content = 1
	return has_parent_content	

def crossover(gens, biggest_gens):
	mask = np.random.randint(8, size=10)
	for i in range(NUMBER_OF_GENES):
		if (not is_parent(gens[i], biggest_gens)):
			gens[i].crossover(mask)
	return gens 		

def run(gens, biggest_gens):
	for gene in gens:
		gene.sell(has_parent_content(gene, biggest_gens))

	[print(gene.get_items_sold()) for gene in gens]
	[market_history.append(gene.get_items_sold()) for gene in gens] 


def plot_genes_market():
	colors = cm.rainbow(np.linspace(0, 1, NUMBER_OF_GENES))
	for gene, c in zip(np.arange(NUMBER_OF_GENES), colors):
		plt.plot( np.arange(EPOCHS), [market_history[gene+i*NUMBER_OF_GENES] for i in range(EPOCHS)])
	plt.show()	

if __name__ == '__main__':
	gens = []
	dis = Discriminator()
	market_history = []

	for gene in range(NUMBER_OF_GENES):
		gens.append(Generator(dis))
	run(gens, [])

	running = 1
	for i in range(EPOCHS):
		gens, biggest_gens = selection(gens)
		gens = crossover(gens, biggest_gens)	
		run(gens, biggest_gens)

	plot_genes_market()