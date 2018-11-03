from Generator import Generator
from Discriminator import Discriminator


if __name__ == '__main__':
	gen = []
	dis = Discriminator()
	
	for i in range(50):
		gen.append(Generator(dis))
	not_sold = 1
	while(not_sold):
		for i in range(50):
			if (gen[i].sell()):
				not_sold = 0

