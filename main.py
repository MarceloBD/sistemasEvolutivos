from Generator import Generator
from Discriminator import Discriminator
import numpy as np 
import copy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

NUMBER_OF_GENES = 50 
EPOCHS = 200


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
	for gene in range(NUMBER_OF_GENES):
		gen[gene].sell()

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
	run(gen)

	running = 1
	for i in range(EPOCHS):
		new_gen = selection(gen)
		#gen = crossover(new_gen)
		gen = new_gen	
		run(gen)

	plot_genes_market(gen)